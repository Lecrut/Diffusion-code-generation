import sys
def calculate_value(choice):
    if choice == 1:
        return "Option A selected"
    elif choice == 2:
        return "Option B selected"
    elif choice >= 3 and choice <= 5:
        print("Error: Please choose between Option C, D, or E.")
        sys.exit(0)
    else:
        print("Invalid input. Expected a number from 1 to 2 (or specific range for others).")
        sys.exit(0)
if __name__ == '__main__':
    sample_choice = 3
    try:
        result = calculate_value(sample_choice)
        if isinstance(result, str):
            print(f"Result: {result}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")