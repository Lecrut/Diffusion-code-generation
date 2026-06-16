import sys
def process_choice(choice):
    valid_choices = ['a', 'b', 'c']
    if not isinstance(choice, str) or len(choice.strip()) == 0:
        raise ValueError("Invalid input type. Please provide a string.")
    normalized_choice = choice.lower().strip()
    try:
        index = valid_choices.index(normalized_choice) + 1
        outputs = {
            'a': "Option A selected.",
            'b': "Option B selected.",
            'c': "Option C selected."
        }
        return outputs[normalized_choice]
    except ValueError:
        raise ValueError(f"Invalid choice '{choice}'. Please select one of the following options.")
def main():
    sample_choices = ['a', 'invalid_input', '', 123, None, 'B']
    for i, user_choice in enumerate(sample_choices):
        try:
            result = process_choice(user_choice)
            print(f"Input {i+1}: '{user_choice}' -> Output: {result}")
        except ValueError as e:
            print(f"Input {i+1}: '{user_choice}' -> Error: {e}")
if __name__ == '__main__':
    main()