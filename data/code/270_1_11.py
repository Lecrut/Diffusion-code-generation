def remove_spaces(s):
    return s.replace(' ', '')

if __name__ == '__main__':
    print(remove_spaces("Hello World"))
    print(remove_spaces("  Leading spaces"))
    print(remove_spaces("Trailing spaces  "))
    print(remove_spaces("Multiple   consecutive spaces"))
    print(remove_spaces(""))
    print(remove_spaces("NoSpacesHere"))