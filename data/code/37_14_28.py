STRING1 = "Hello"
STRING2 = "World"

def concatenate_strings(str1, str2):
    result = ""
    result += str1
    result += str2
    return result

if __name__ == '__main__':
    concatenated_result = concatenate_strings(STRING1, STRING2)
    print(concatenated_result)