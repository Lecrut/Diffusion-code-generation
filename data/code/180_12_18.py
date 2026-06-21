def is_word_in_list(word, string_list):
    return word.lower() in {s.lower() for s in string_list}

if __name__ == '__main__':
    sample_word = 'example'
    sample_list = ['Example', 'test', 'sample', 'EXAMPLE']
    print(is_word_in_list(sample_word, sample_list))