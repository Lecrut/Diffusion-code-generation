def word_exists_in_sequence(word, sequence):
    return any(w == word for w in sequence)

if __name__ == '__main__':
    sample_word = 'hello'
    sample_sequence = ['world', 'hello', 'python']
    print(word_exists_in_sequence(sample_word, sample_sequence))