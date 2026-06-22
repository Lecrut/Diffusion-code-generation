def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    result = replace_spaces_with_underscores("Hello World")
    print(result)