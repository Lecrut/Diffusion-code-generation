import sys
def get_user_choice():
    valid_options = ['a', 'b', 'c']
    while True:
        try:
            user_input = input("Select an option (A/B/C): ").strip().lower()
            if not user_input or len(user_input) > 1:
                print("Error: Please enter exactly one character.")
                continue
            if user_input in valid_options:
                return user_input
            else:
                print(f"Error: Invalid option. Choose from {valid_options}.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            sys.exit(0)
        except EOFError:
            print("\nNo input received.")
            sys.exit(1)
def make_decision(choice):
    decisions = {
        'a': "Decision made based on option A.",
        'b': "Decision made based on option B.",
        'c': "Decision made based on option C."
    }
    return decisions.get(choice, "Error: Unknown decision logic.")
if __name__ == '__main__':
    test_cases = ['a', 'b', 'c']
    print("Running Decision-Making Script with Sample Inputs...")
    for choice in test_cases:
        result = make_decision(choice)
        print(f"Input: {choice} -> Output: {result}")
    try:
        invalid_input = "x"
        if invalid_input not in ['a', 'b', 'c']:
            print("Handled Invalid Input Scenario")
    except Exception as e:
        print(f"Unexpected Error during simulation: {e}")
    print("Script execution completed successfully.")