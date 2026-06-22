MAX_WORD_LENGTH = 100

def extract_words(sentence):
    return sentence.split()

def find_longest_word(words):
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length and len(word) <= MAX_WORD_LENGTH:
            longest_word = word
            max_length = len(word)
    return longest_word

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    words = extract_words(sample_sentence)
    print(find_longest_word(words))