def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    print(replace_spaces_with_underscores("Hello World"))