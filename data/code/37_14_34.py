def concatenate_strings(str1, str2):
    result = ""
    for part in (str1, str2):
        if not isinstance(part, str):
            raise ValueError("Both inputs must be strings")
        result += part
    return result

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "World"
    concatenated_result = concatenate_strings(string1, string2)
    print(concatenated_result)