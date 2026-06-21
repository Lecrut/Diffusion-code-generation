def validate_numeric_strings(numeric_strings):
    if not all(isinstance(s, str) and s.isdigit() for s in numeric_strings):
        raise ValueError("All elements must be numeric strings")

def sort_numeric_strings(numeric_strings):
    validate_numeric_strings(numeric_strings)
    return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numeric_strings(sample_values))