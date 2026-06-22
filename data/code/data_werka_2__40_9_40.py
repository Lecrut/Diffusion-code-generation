def validate_input(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list.")
    for s in strings:
        if not isinstance(s, str):
            raise ValueError("All elements in the list must be strings.")

def get_first_letters(strings):
    validate_input(strings)
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_values = ["strawberry", "tangerine", "lime", "lemon"]
    result = get_first_letters(sample_values)
    print(result)