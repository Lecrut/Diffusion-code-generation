def lexicographical_comparison(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_str1 = "banana"
    sample_str2 = "apple"
    comparison_result = lexicographical_comparison(sample_str1, sample_str2)
    print(comparison_result)