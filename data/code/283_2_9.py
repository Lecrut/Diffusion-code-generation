def count_non_strings(string_list):
    non_string_count = 0
    for element in string_list:
        if not isinstance(element, str):
            non_string_count += 1
    return non_string_count

if __name__ == '__main__':
    sample_list = ["Hello Python world", "Java programming", 42, "Python is fun", None, "Another Python example"]
    result = count_non_strings(sample_list)
    print(result)