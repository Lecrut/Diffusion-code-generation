def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return " ".join(reversed_words)

if __name__ == "__main__":
    sample_sentence = "Hello world this is a test"
    result = reverse_words(sample_sentence)
    print(result)