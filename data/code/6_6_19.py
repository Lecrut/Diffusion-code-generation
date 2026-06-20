def convert_spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    result = convert_spaces_to_underscores("hello world this is a test")
    print(result)