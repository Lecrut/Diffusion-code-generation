def join_strings(str1, str2):
    return f"{str1} {str2}"

if __name__ == '__main__':
    GREETING = "Hello"
    FAREWELL = "Goodbye"
    result = join_strings(GREETING, FAREWELL)
    print(result)