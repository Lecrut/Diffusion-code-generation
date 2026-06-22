def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    sample_sentence = "apple banana apple orange banana apple"
    result = count_word_occurrences(sample_sentence)
    print(result)