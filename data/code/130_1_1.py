import sys
sample_number = 0
if __name__ == '__main__':
    try:
        user_input = input("Enter a number: ")
        entered_number = float(user_input)
        if entered_number == 0:
            print("The entered number is zero.")
        else:
            print("The entered number is not zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")