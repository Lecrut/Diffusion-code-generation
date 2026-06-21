def reverse_word_order(text):
    words = text.split()
    reversed_words = list(reversed(words))
    return " ".join(reversed_words)

if __name__ == '__main__':
    test_string1 = "AI helps coding"
    result1 = reverse_word_order(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: '{result1}'")