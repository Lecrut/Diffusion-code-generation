def extract_words(sentence):
    return sentence.split()

def find_longest_word(words):
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

def longest_word(sentence):
    words = extract_words(sentence)
    return find_longest_word(words)

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(longest_word(sample_sentence))