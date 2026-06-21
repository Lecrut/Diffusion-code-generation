def compare_strings(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    STR1 = "zebra"
    STR2 = "apple"
    result = compare_strings(STR1, STR2)
    print(result)