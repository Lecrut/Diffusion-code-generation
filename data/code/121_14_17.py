def later_string(s1, s2):
    if s1 > s2:
        return s1
    else:
        return s2

if __name__ == '__main__':
    string1 = "cherry"
    string2 = "banana"
    result = later_string(string1, string2)
    print(result)