def validate_input(data):
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All elements must be strings representing integers.")
    
    if not data:
        raise ValueError("The list cannot be empty.")

def find_smallest_int_string(strings):
    validate_input(strings)
    return min(strings, key=int)

if __name__ == '__main__':
    sample_strings = ["3", "15", "2", "9"]
    result = find_smallest_int_string(sample_strings)
    print(result)