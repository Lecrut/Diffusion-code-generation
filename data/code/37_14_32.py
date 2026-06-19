def concatenate_strings(str1, str2):
    result = ""
    for char in str1:
        result += char
    for char in str2:
        result += char
    return result

if __name__ == '__main__':
    STRING_LITERAL_1 = "Hello"
    STRING_LITERAL_2 = "World"
    concatenated_result = concatenate_strings(STRING_LITERAL_1, STRING_LITERAL_2)
    print(concatenated_result)