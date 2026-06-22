def spaces_to_underscores(input_string):
    return input_string.replace(' ', '_')

if __name__ == '__main__':
    sample = "hello world this is a test"
    print(spaces_to_underscores(sample))