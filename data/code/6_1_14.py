def spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "hello world foo bar"
    result = spaces_to_underscores(sample_string)
    print(result)