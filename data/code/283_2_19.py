def count_non_strings(input_list):
    non_string_count = 0
    for item in input_list:
        if not isinstance(item, str):
            non_string_count += 1
    return non_string_count

if __name__ == '__main__':
    sample_list = ["Hello Python world", "Java programming", 42, True, "Python is fun"]
    result = count_non_strings(sample_list)
    print(result)