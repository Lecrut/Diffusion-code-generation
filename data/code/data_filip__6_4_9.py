def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    print(replace_spaces_with_underscores('hello world'))
    print(replace_spaces_with_underscores('python programming'))
    print(replace_spaces_with_underscores('no spaces'))
    print(replace_spaces_with_underscores('multiple   spaces'))
    print(replace_spaces_with_underscores(''))