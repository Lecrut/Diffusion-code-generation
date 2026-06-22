def compare_strings(str1, str2):
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    print(compare_strings('Hello', 'hello'))
    print(compare_strings('Python', 'PYTHON'))
    print(compare_strings('World', 'world!'))