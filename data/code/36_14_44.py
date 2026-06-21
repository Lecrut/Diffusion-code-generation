def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "OpenAI is creating innovative tools"
    print(reverse_sentence(sample_sentence))