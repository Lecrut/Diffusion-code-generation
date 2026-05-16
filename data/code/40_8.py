def first_letters(text):
    words = text.split()
    result = []
    for word in words:
        if word and any(char.isalpha() for char in word):
            result.append(word[0])
    return result
if __name__ == '__main__':
    test_cases = [
        "Hello world",
        "This is a test sentence.",
        "Word1, Word2. Word3!",
        "  leading spaces and trailing spaces  ",
        "  ... ! ?  ",
        "Only",
        "  ",
        "  . , ! "
    ]
    for text in test_cases:
        output = first_letters(text)
        print(f"Input: '{text}'")
        print(f"Output: {output}\n")