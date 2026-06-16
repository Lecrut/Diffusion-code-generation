import sys
def calculate_output(choice: int) -> str:
    if not isinstance(choice, (int, float)):
        return "Error: Input must be a number."
    try:
        numeric_choice = int(float(choice))
        if 1 <= numeric_choice <= 3:
            message_map = {
                1: "You chose option one.",
                2: "You chose option two.",
                3: "You chose option three."
            }
            return message_map.get(numeric_choice, f"Unknown choice within range.")
        elif numeric_choice == 0 or -9 <= numeric_choice < 1:
            return "Error: Invalid negative input detected."
        else:
            return f"Warning: Input exceeds expected maximum of 3. Value received: {numeric_choice}."
    except (ValueError, OverflowError):
        return "Error: Unable to convert input to a valid integer."
if __name__ == '__main__':
    sample_inputs = [1, -5, 0, 4, 'abc', float('inf'), None]
    for test_input in sample_inputs:
        result = calculate_output(test_input)
        print(f"Input: {test_input!r} -> Output: {result}")