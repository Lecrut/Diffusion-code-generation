def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    sample_sentence = "hello world hello python"
    result = count_word_occurrences(sample_sentence)
    print(result)