def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_string = "the quick brown fox"
    result = reverse_words(sample_string)
    print(result)