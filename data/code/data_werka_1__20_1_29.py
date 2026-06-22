def case_insensitive_equals(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    result = case_insensitive_equals("Hello", "hello")
    print(result)