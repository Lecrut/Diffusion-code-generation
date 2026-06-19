def lexicographic_compare(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_str1 = "apple"
    sample_str2 = "banana"
    result = lexicographic_compare(sample_str1, sample_str2)
    print(result)