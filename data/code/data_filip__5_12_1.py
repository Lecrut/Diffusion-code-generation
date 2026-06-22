def title_case_first(s):
    return s[:1].upper() + s[1:].lower()

if __name__ == '__main__':
    print(title_case_first('hello'))
    print(title_case_first('WORLD'))
    print(title_case_first('hElLo WoRlD'))
    print(title_case_first(''))
    print(title_case_first('a'))