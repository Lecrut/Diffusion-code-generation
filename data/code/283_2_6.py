def count_non_string_elements(input_list):
    non_string_count = 0
    for element in input_list:
        if not isinstance(element, str):
            non_string_count += 1
    return non_string_count

if __name__ == '__main__':
    sample_list = ["Hello Python world", "Java programming", 42, True, "Python is fun", 3.14]
    result = count_non_string_elements(sample_list)
    print(result)