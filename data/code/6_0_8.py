def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    print(replace_spaces_with_underscores("Hello World"))
    print(replace_spaces_with_underscores("Python is great"))
    print(replace_spaces_with_underscores("NoSpaces"))
    print(replace_spaces_with_underscores("   Multiple   Spaces   "))