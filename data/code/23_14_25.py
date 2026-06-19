def compare_strings(s1, s2):
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    string1 = "apple"
    string2 = "banana"
    result = compare_strings(string1, string2)
    print(result)