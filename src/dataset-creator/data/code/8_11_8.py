def evaluate_conditions(user_input: str) -> None:
    if user_input.lower() in ("yes", "y"):
        print("Confirmation received.")
    elif len(user_input.strip()) == 0:
        print("Input is empty.")
    else:
        try:
            number = int(user_input)
            if number > 100:
                print(f"Number {number} exceeds limit.")
            else:
                print(f"Valid number within range: {number}")
        except ValueError:
            print("Input is not a valid integer.")
if __name__ == '__main__':
    sample_input = "150"
    evaluate_conditions(sample_input)