def count_non_string_elements(input_list):
    if not all(isinstance(item, str) for item in input_list):
        raise ValueError("All elements in the list must be strings")
    
    non_string_count = sum(not isinstance(item, str) for item in input_list)
    return non_string_count

if __name__ == '__main__':
    sample_list = ["Hello Python world", 123, "Java programming", True, "Python is fun"]
    result = count_non_string_elements(sample_list)
    print(result)