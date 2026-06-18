import sys
def get_user_choice():
    try:
        user_input = int(input("Select an option (1-3): "))
        if not 1 <= user_input <= 3:
            print("Error: Please select a number between 1 and 3.")
            return None
        return user_input
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
def make_decision(choice):
    if choice == 1:
        result = "Option A selected."
    elif choice == 2:
        result = "Option B selected."
    else:
        result = "Option C selected."
    print(f"Decision made: {result}")
if __name__ == '__main__':
    test_cases = [1, 2, 3, 5, -1] 
    for case in test_cases:
        user_input = str(case)
        try:
            choice_value = int(user_input) if isinstance(user_input, str) else user_input
            valid_choice = None
            if 1 <= choice_value <= 3:
                valid_choice = choice_value
        except ValueError:
            print(f"Error processing case {case}: Not a number.")
        try:
            decision_result = make_decision(valid_choice)
        except Exception as e:
            print(f"Unexpected error during decision making for input {valid_choice}: {e}")
def run_simulation():
    sample_inputs = ["1", "2", "3", "abc", "-5"] 
    for inp_str in sample_inputs:
        try:
            choice = int(inp_str)
            if 1 <= choice <= 3:
                print(f"Input '{inp_str}' -> Valid Choice {choice}")
                make_decision(choice)
            else:
                print(f"Input '{inp_str}' -> Invalid Range")
        except ValueError as ve:
            print(f"Input '{inp_str}' -> Value Error (not an integer)")