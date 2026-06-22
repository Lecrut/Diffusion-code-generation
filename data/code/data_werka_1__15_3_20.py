def compare_strings(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    result = compare_strings("Hello", "hello")
    print(result)