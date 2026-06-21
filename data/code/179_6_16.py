def reverse_words(text):
    words = text.split()
    reversed_text = ' '.join(words[::-1])
    return reversed_text

if __name__ == '__main__':
    sample_text = "Python is fun to learn"
    reversed_sentence = reverse_words(sample_text)
    print(reversed_sentence)