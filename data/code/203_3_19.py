def compare_strings(str1, str2):
    return str1 < str2

if __name__ == '__main__':
    sample_str1 = "apple"
    sample_str2 = "banana"
    if not isinstance(sample_str1, str) or not isinstance(sample_str2, str):
        raise ValueError("Both inputs must be strings")
    result = compare_strings(sample_str1, sample_str2)
    print(result)