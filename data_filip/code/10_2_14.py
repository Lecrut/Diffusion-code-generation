def reverse_words(sentence):
    if sentence is None:
        return ""
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello    world  this   is   a   test"
    result = reverse_words(sample_sentence)
    print(result)