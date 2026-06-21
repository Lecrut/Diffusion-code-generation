def word_exists(word, sequence):
    return any(w == word for w in sequence)

if __name__ == '__main__':
    sample_word = 'hello'
    sample_sequence = ['world', 'python', 'hello', 'programming']
    print(word_exists(sample_word, sample_sequence))