def validate_numeric_strings(numeric_strings):
    for value in numeric_strings:
        if not value.isdigit():
            raise ValueError(f"Invalid numeric string: {value}")

def sort_numeric_strings(numeric_strings):
    validate_numeric_strings(numeric_strings)
    return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numeric_strings(sample_values))