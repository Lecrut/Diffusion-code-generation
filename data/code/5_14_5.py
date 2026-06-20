def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "PYTHON Programming IS Fun"
    sample3 = "  spaces   everywhere  "
    sample4 = "already Capitalized Words"

    print(capitalize_words(sample1))
    print(capitalize_words(sample2))
    print(capitalize_words(sample3))
    print(capitalize_words(sample4))