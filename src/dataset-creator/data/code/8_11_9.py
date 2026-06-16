def evaluate_conditions(user_input: str) -> None:
    if user_input.lower() in ("yes", "y"):
        print("Confirmation received.")
    elif user_input.isdigit():
        number = int(user_input)
        if 1 <= number <= 100:
            print(f"Valid integer entered: {number}")
        else:
            print("Integer out of range [1, 100].")
    elif "error" in user_input.lower():
        raise ValueError("An error condition was detected.")
    else:
        print("No specific action triggered for this input.")
if __name__ == '__main__':
    sample_inputs = ["yes", "42", "hello world", "150"]
    for test_input in sample_inputs:
        try:
            evaluate_conditions(test_input)
        except ValueError as e:
            print(f"Exception occurred: {e}")