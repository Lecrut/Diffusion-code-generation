def split_and_reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return reversed_words

if __name__ == '__main__':
    sample_sentence1 = "This is an example sentence for testing"
    result1 = split_and_reverse(sample_sentence1)
    print(result1)

    sample_sentence2 = "Another test case with spaces and punctuation!"
    result2 = split_and_reverse(sample_sentence2)
    print(result2)