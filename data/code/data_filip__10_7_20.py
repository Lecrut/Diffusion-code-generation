def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    index = len(words) - 1
    while index >= 0:
        reversed_words.append(words[index])
        index -= 1
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello World from Python"
    result = reverse_words(sample_sentence)
    print(result)