def concatenate_strings(str1, str2):
    result = ""
    result += str1
    result += str2
    return result

if __name__ == '__main__':
    string1 = "Hello, "
    string2 = "World!"
    concatenated_result = concatenate_strings(string1, string2)
    print(concatenated_result)