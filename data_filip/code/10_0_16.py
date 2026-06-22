def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    result = reverse_sentence(sample_text)
    print(result)