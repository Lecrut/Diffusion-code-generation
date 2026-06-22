def concatenate_strings(str1, str2):
    return ''.join((str1, str2))

if __name__ == '__main__':
    STRING_A = "Hello"
    STRING_B = ", World!"
    result = concatenate_strings(STRING_A, STRING_B)
    print(result)