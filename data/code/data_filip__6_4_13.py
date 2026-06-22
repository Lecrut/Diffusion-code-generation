def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    print(replace_spaces_with_underscores("hello world"))
    print(replace_spaces_with_underscores("python is great"))
    print(replace_spaces_with_underscores("no_spaces_here"))
    print(replace_spaces_with_underscores("multiple   spaces   here"))