def validate_elements(input_list):
    non_string_count = sum(not isinstance(item, str) for item in input_list)
    if any(isinstance(item, str) and 'Python' not in item for item in input_list):
        raise ValueError("Input list contains non-string elements or strings without 'Python'")
    return non_string_count

def count_non_python_strings(string_list):
    non_string_count = validate_elements(string_list)
    python_count = len([s for s in string_list if 'Python' in s])
    return python_count

if __name__ == '__main__':
    sample_list = ["Hello Python world", "Java programming", "Python is fun", "C++ development", "Another Python example"]
    result = count_non_python_strings(sample_list)
    print(result)