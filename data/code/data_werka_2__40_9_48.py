def get_first_letters(strings):
    def validate_strings(input_list):
        if not all(isinstance(s, str) for s in input_list):
            raise ValueError("All elements in the input list must be strings.")
        if any(len(s) == 0 for s in input_list):
            raise ValueError("No empty strings are allowed in the input list.")

    validate_strings(strings)
    return [s[0] for s in strings]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = get_first_letters(sample_values)
    print(result)