def compare_strings(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    sample_str1 = "Hello World"
    sample_str2 = "hello world"
    result = compare_strings(sample_str1, sample_str2)
    print(result)