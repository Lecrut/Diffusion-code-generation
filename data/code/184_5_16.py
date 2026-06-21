def case_insensitive_match(word, word_list):
    lower_word = word.lower()
    return any(lower_word == w.lower() for w in word_list)

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python3', 'ruby']
    match_result = case_insensitive_match(sample_word, sample_list)
    print(match_result)