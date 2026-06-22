def case_insensitive_equal(str1, str2):
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    sample_str1 = "Hello World"
    sample_str2 = "hello world"
    result = case_insensitive_equal(sample_str1, sample_str2)
    print(result)