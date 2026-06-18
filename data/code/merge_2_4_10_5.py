def process_choice(choice):
    try:
        choice = int(choice)
        if 1 <= choice <= 3:
            return f"Processing option {choice}..."
        elif choice == 4:
            print("Exiting the program.")
            return None
        else:
            raise ValueError(f"Invalid input. Expected a number between 1 and 4, got {choice}.")
    except (ValueError, TypeError):
        print("Input must be an integer.")
        return "Handling invalid data type..."
if __name__ == '__main__':
    test_cases = [
        "2",
        "-5",
        "abc",
        "",
        3.14,
        None
    ]
    for input_val in test_cases:
        result = process_choice(input_val)
        print(f"Input: {input_val} -> Output: {result}")