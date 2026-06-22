def combine_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    GREETING = "Hello"
    SUBJECT = "World"
    result = combine_strings(GREETING, SUBJECT)
    print(result)