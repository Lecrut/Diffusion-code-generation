def concatenate_strings(str1, str2):
    result = ""
    for char in str1:
        result += char
    for char in str2:
        result += char
    return result

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "World"
    concatenated_result = concatenate_strings(string1, string2)
    print(concatenated_result)