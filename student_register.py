"""This program allows the user to register student IDs for an exam 
prints and then saves a textfile of a register."""

import os
import time
import sys

# Function used to clear screen for cleaner output on terminal.
def clear_screen(time_delay):
    """Function to clear terminal."""
    time.sleep(time_delay)
    os.system("clear||cls")
clear_screen(0)

# Prompt user to enter the number of students.
STUDENT_NUM_COLLECTED = False
STUDENT_NUM = 0
INVALID_INPUT = 0
while INVALID_INPUT < 5 and not STUDENT_NUM_COLLECTED:
    print("STUDENT REGISTER PROGRAM".center(40, '='))
    if INVALID_INPUT > 0:
        print(f"\nAttempts: {INVALID_INPUT}\nNote: program quits after 5 attempts.")
    STUDENT_NUM = input("\nEnter Number of Students: ").strip()
    # Error handling: only accepts 1-2 digit numbers from 0-99.
    if STUDENT_NUM.isdigit() and int(STUDENT_NUM) > 0 and int(STUDENT_NUM) <= 99:
        print(f"\033[92mNumber of Students: {STUDENT_NUM}\033[0m")
        STUDENT_NUM_COLLECTED = True
        clear_screen(1.3)
    else:
        print("\033[91mError: Please enter a 1-2 digit number from 0-99.\033[0m")
        INVALID_INPUT += 1
        clear_screen(2)
# After 5 incorrect attempts, program will quit.
if INVALID_INPUT == 5:
    print("\n\033[91mError: 5 incorrect attempts. Exiting Program.\033[0m")

# Prompt user to enter student ID information.
student_info = {}
if STUDENT_NUM_COLLECTED:
    TO_ENTER = int(STUDENT_NUM) # Variable for displaying IDs numbers left to enter.
    STUDENT_COUNT = int(STUDENT_NUM) + 1
    # Iterate through number of students provided by user.
    for student in (range(1, STUDENT_COUNT)):
        # Prompt user for input until a correct ID number is entered.
        VALID_INPUT = False
        while not VALID_INPUT:
            # Print program info.
            print(f"\033[92mNumber of Students: {STUDENT_NUM}\033[0m")
            print("Enter 4-digit ID number for each student. For example '0394'.")
            print("Type 'exit' to quit program.")

            # Print dictionary once ID entered.
            if student_info:
                print('')
                for key, value in student_info.items():
                    print(f"Student {key}: ID #{value}")

            # Get input.
            print(f"\n\033[92mStudent ID Numbers left to enter: {TO_ENTER}\033[0m")
            id_num = input(f"Enter Student {student} ID: ").strip()
            # Exit program option.
            if id_num.lower() == "exit":
                print("\033[91mExiting program.\033[0m")
                sys.exit()
            # Only accept 4 digits.
            if id_num.isdigit() and len(str(id_num)) == 4:
                # If Student / ID number are not in dictionary, enter them.
                if id_num not in student_info.values():
                    student_info[student] = id_num
                    TO_ENTER -= 1
                    print(f"\033[92mStudent ID {id_num} successfully entered into system.\033[0m")
                    # Break loop and continue to next student.
                    VALID_INPUT = True
                    clear_screen(1.5)
                else:
                    print(f"\033[91mID number '{id_num}' has already been entered.\033[0m")
                    clear_screen(2)
            else:
                print(f"\033[91mError: type 4-digit number for Student ID. Not '{id_num}'.\033[0m")
                clear_screen(2)

if student_info:
    # Print information to terminal.
    print('=' * 40)
    print("STUDENT #ID".ljust(13) + "EXAM REGISTER" + "SIGN NAME".rjust(13))
    print('=' * 40 + "\n")
    for key, value in student_info.items():
        print(f"Student {key}: ID #{value} ".ljust(40, '.'))
        print('')

    # Print student information in output text file.
    try:
        with open('reg_form.txt', 'w', encoding='utf-8') as file:
            file.write('=' * 40 + '\n')
            file.write("STUDENT #ID".ljust(13) + "EXAM REGISTER" + "SIGN NAME".rjust(13) + '\n')
            file.write('=' * 40 + "\n\n")
            for key, value in student_info.items():
                file.write(f"Student {key}: ID #{value} ".ljust(40, '.') + '\n\n')
            file.write('=' * 40 + '\n')
            print("\033[92mStudent register successfully generated in 'reg_form.txt'.\033[0m")
    # General exception to catch error, as I don't expect one to occur.
    except PermissionError:
        print("Error: Permission denied. Unable to write to 'reg_form.txt'.")
    except IOError as e:
        print(f"An error occurred: {e}")
