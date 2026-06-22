def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample = "hello world this is a test"
    print(replace_spaces_with_underscores(sample))