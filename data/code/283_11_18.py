def validate_input(data):
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All elements must be strings")

def ensure_strings(lst):
    return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = ['apple', 42, 'banana', 3.14]
    validate_input(sample_list)
    result = ensure_strings(sample_list)
    print(result)