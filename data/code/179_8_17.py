def reverse_word_order(text):
    words = text.split()
    return " ".join(reversed(words))

if __name__ == '__main__':
    test_string1 = "AI helps coding"
    result = reverse_word_order(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: '{result}'")