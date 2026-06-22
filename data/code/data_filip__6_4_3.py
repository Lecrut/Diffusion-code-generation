def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    print(replace_spaces_with_underscores('hello world'))