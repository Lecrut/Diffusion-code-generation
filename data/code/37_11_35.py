def concatenate_strings(str1, str2):
    return f"{str1}{str2}"

if __name__ == '__main__':
    GREETING = "Hello"
    TARGET = "World"
    result = concatenate_strings(GREETING, TARGET)
    print(result)