def case_insensitive_match(word, word_list):
    if not isinstance(word, str) or not all(isinstance(w, str) for w in word_list):
        raise ValueError("Invalid input: 'word' must be a string and 'word_list' must be a list of strings.")
    return any(w.lower() == word.lower() for w in word_list)

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python', 'ruby']
    print(case_insensitive_match(sample_word, sample_list))