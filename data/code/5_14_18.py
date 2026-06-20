def capitalize_words(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "PYTHON is GREAT"
    sample3 = "   multiple   spaces   "
    print(capitalize_words(sample1))
    print(capitalize_words(sample2))
    print(capitalize_words(sample3))