def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings")
    return str1 + str2

if __name__ == '__main__':
    first_string = "Good morning, "
    second_string = "Alibaba Cloud!"
    combined_result = combine_strings(first_string, second_string)
    print(combined_result)