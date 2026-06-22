def lexicographic_compare(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_string1 = "kiwi"
    sample_string2 = "mango"
    comparison_result = lexicographic_compare(sample_string1, sample_string2)
    print(comparison_result)