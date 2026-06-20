def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON is AWESOME",
        "capitalize   this",
        "",
        "a"
    ]
    for s in sample_strings:
        print(capitalize_words(s))