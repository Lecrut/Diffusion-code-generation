def lexicographical_compare(str1, str2):
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    sample_str1 = "cherry"
    sample_str2 = "banana"
    comparison_result = lexicographical_compare(sample_str1, sample_str2)
    print(comparison_result)