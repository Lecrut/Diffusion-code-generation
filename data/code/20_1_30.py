def case_insensitive_equal(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    result = case_insensitive_equal("Hello", "hello")
    print(result)