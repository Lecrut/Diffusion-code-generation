def capitalize_words(s):
    return s.title()

if __name__ == '__main__':
    sample = "hello world foo bar"
    print(capitalize_words(sample))
    sample2 = "PYTHON Is AWESOME"
    print(capitalize_words(sample2))
    sample3 = "mixed CASE string"
    print(capitalize_words(sample3))