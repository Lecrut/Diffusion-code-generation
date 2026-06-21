def validate_numerical_strings(strings):
    if not all(string.isdigit() for string in strings):
        raise ValueError("All elements must be numerical strings")

def sort_numerical_strings(numerical_strings):
    validate_numerical_strings(numerical_strings)
    return sorted(map(int, numerical_strings))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numerical_strings(sample_values))