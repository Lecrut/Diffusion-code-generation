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
            print("\nProgram terminated by user.")
            sys.exit(0)
        except EOFError:
            print("Input stream ended unexpectedly.")
            sys.exit(0)
def make_decision(choice):
    decisions = {
        'a': "Decision made based on option A.",
        'b': "Decision made based on option B.",
        'c': "Decision made based on option C."
    }
    return decisions.get(choice, "Error: Unknown decision path.")
if __name__ == '__main__':
    choices = ['a', 'b'] 
    for choice in choices:
        result = make_decision(choice)
        print(f"Result for {choice}: {result}")