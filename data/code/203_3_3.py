def compare_strings(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_str1 = "zebra"
    sample_str2 = "apple"
    result = compare_strings(sample_str1, sample_str2)
    print(result)