def split_sentence(sentence):
    return sentence.split()

def validate_words(words):
    if not words:
        raise ValueError("Input sentence is empty or contains only spaces.")

def find_longest_word(words):
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word

def longest_word(sentence):
    words = split_sentence(sentence)
    validate_words(words)
    return find_longest_word(words)

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(longest_word(sample_sentence))