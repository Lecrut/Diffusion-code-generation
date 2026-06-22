def validate_elements(data):
    for item in data:
        if not isinstance(item, str):
            return False
    return True

def ensure_strings(lst):
    return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = ['apple', 42, 'banana', 3.14]
    if not validate_elements(sample_list):
        sample_list = ensure_strings(sample_list)
    result = all(isinstance(item, str) for item in sample_list)
    print(result)