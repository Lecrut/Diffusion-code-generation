def later_string(s1, s2):
    if s1 > s2:
        return s1
    else:
        return s2

if __name__ == '__main__':
    str1 = "cherry"
    str2 = "banana"
    result = later_string(str1, str2)
    print(result)