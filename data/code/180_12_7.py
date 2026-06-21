def is_word_in_list(word, word_list):
    return word.lower() in {w.lower() for w in word_list}

if __name__ == '__main__':
    sample_word = 'example'
    sample_list = ['Example', 'test', 'sample', 'EXAMPLE']
    print(is_word_in_list(sample_word, sample_list))