def spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    result = spaces_to_underscores(sample_text)
    print(result)