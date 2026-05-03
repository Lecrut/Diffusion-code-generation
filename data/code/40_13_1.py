def get_first_letter(s):
    if not s:
        return ""
    return s[0]
if __name__ == '__main__':
    print(get_first_letter("hello"))
    print(get_first_letter(""))
    print(get_first_letter("a"))
    print(get_first_letter(" "))