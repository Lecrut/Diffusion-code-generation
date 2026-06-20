def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return ' '.join(reversed_words)

if __name__ == '__main__':
    text = "Hello World from Python"
    result = reverse_words_in_sentence(text)
    print(result)