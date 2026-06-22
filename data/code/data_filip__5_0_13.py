def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "HELLO WORLD"
    sample3 = "hElLo WoRlD"
    sample4 = ""
    sample5 = "a"
    print(capitalize_first_letter(sample1))
    print(capitalize_first_letter(sample2))
    print(capitalize_first_letter(sample3))
    print(capitalize_first_letter(sample4))
    print(capitalize_first_letter(sample5))