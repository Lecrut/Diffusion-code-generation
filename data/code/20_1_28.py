def case_insensitive_compare(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "hello"
    result = case_insensitive_compare(string1, string2)
    print(result)