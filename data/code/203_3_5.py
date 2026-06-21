def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return str1 < str2

if __name__ == '__main__':
    sample_str1 = "apple"
    sample_str2 = "banana"
    result = compare_strings(sample_str1, sample_str2)
    print(result)