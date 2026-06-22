def merge_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    first_string = "Good"
    second_string = "Morning"
    combined_result = merge_strings(first_string, second_string)
    print(combined_result)