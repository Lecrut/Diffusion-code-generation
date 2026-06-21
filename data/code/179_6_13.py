def reverse_words(text):
    words = text.split()
    reversed_words = [words[i] for i in range(len(words)-1, -1, -1)]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words(sample_text))