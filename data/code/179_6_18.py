def reverse_words(text):
    words = text.split()
    if not words:
        return ""
    reversed_text = ' '.join(words[::-1])
    return reversed_text

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words(sample_text))