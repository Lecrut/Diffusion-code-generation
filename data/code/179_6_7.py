def reverse_words(text):
    words = text.split()
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings")
    reversed_text = ' '.join(words[::-1])
    return reversed_text

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words(sample_text))