def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    
    longest_word = words[0]
    max_length = len(longest_word)
    
    for word in words[1:]:
        current_length = len(word)
        if current_length > max_length:
            longest_word = word
            max_length = current_length
    
    return longest_word

if __name__ == '__main__':
    sample_sentence = "A quick brown fox jumps over the lazy dog"
    print(find_longest_word(sample_sentence))