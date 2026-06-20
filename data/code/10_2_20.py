def reverse_words(sentence):
    if not sentence:
        return sentence
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    sample_sentence = "  Hello    world  this   is   a   test  "
    result = reverse_words(sample_sentence)
    print(result)