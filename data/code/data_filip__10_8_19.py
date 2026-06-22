def reverse_words(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_input = "Hello world this is a high performance task"
    result = reverse_words(sample_input)
    print(result)