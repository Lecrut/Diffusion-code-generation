def remove_spaces(s):
    return s.replace(" ", "")

if __name__ == '__main__':
    print(remove_spaces("Hello World"))
    print(remove_spaces("  Leading and trailing spaces  "))
    print(remove_spaces("Multiple   consecutive   spaces"))