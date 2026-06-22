def combine_strings(str1, str2):
    return f"{str1} {str2}"

if __name__ == '__main__':
    first_part = "Good morning"
    second_part = "Everyone"
    combined_message = combine_strings(first_part, second_part)
    print(combined_message)