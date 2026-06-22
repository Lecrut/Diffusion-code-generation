def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    print(capitalize_words("hello world"))
    print(capitalize_words("PYTHON programming is FUN"))
    print(capitalize_words("multiple   spaces   here"))