def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_text = "The quick brown fox"
    result = reverse_sentence(sample_text)
    print(result)