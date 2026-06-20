def lexicographical_compare(str1, str2):
    for char1, char2 in zip(str1, str2):
        if char1 < char2:
            return -1
        elif char1 > char2:
            return 1
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    return 0

if __name__ == '__main__':
    sample_str1 = "banana"
    sample_str2 = "apple"
    comparison_result = lexicographical_compare(sample_str1, sample_str2)
    print(comparison_result)