def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    print(replace_spaces_with_underscores("hello world"))
    print(replace_spaces_with_underscores("foo bar baz"))
    print(replace_spaces_with_underscores("no spaces here"))
    print(replace_spaces_with_underscores("  leading and trailing  "))
    print(replace_spaces_with_underscores(""))
    print(replace_spaces_with_underscores("single"))