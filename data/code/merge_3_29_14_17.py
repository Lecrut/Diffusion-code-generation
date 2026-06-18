def reverse_word(word):
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access
    samples = [
        "hello",
        "Python",
        "world"
    ]

    for test_word in samples:
        reversed_word = reverse_word(test_word)
        print(f"Original word: {test_word}")
        print("Reversed word:", reversed_word)
        print("-" * 20)