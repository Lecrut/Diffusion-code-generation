def concatenate_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    first_string = "Hello"
    second_string = ", World!"
    combined_result = concatenate_strings(first_string, second_string)
    print(combined_result)