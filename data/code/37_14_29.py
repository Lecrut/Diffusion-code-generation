def concatenate_strings(str1, str2):
    result = ""
    for char in str1:
        result += char
    for char in str2:
        result += char
    return result

if __name__ == '__main__':
    first_part = "Goodbye"
    second_part = "Universe"
    combined_message = concatenate_strings(first_part, second_part)
    print(combined_message)