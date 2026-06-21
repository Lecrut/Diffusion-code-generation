def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    test_string1 = "hello world"
    print(f"Input: '{test_string1}'")
    print(f"Output: '{reverse_words(test_string1)}'")