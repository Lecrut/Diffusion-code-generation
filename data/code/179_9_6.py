def reverse_words(text):
    words = text.split()
    reversed_words = []
    for word in words:
        if word.strip():
            reversed_words.append(word)
    reversed_words.reverse()
    return ' '.join(reversed_words)
if __name__ == '__main__':
    sample_text = 'Hello world from Python'
    print(reverse_words(sample_text))