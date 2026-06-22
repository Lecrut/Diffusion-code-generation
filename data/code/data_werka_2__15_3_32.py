def compare_strings(str1, str2):
    return normalize_case(str1) == normalize_case(str2)

def normalize_case(s):
    return s.lower()

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "hello"
    result = compare_strings(sample_str1, sample_str2)
    print(result)

    additional_test1 = ("Python", "PYTHON")
    additional_test2 = ("World", "world!")
    
    print(compare_strings(*additional_test1))
    print(compare_strings(*additional_test2))