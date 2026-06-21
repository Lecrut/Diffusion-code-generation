def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_string1 = "hello world this is a test"
    print(f"Input: '{sample_string1}'")
    print(f"Output: '{reverse_words(sample_string1)}'")