def evaluate_conditions(user_input: str) -> None:
    if user_input.lower() in ("yes", "y"):
        print("Confirmation received.")
    elif user_input.isdigit():
        number = int(user_input)
        if 1 <= number <= 100:
            print(f"Valid range. Value is {number}.")
        else:
            print("Number out of valid range.")
    elif "error" in user_input.lower() or "fail" in user_input.lower():
        print("Critical alert triggered.")
    else:
        print("No specific condition met.")
if __name__ == '__main__':
    sample_inputs = ["yes", "42", "hello world", "501"]
    for test_case in sample_inputs:
        evaluate_conditions(test_case)