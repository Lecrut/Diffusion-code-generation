def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    print(capitalize_words(sample_string))