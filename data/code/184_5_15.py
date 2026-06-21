def case_insensitive_match(word, word_list):
    if not isinstance(word, str) or not all(isinstance(w, str) for w in word_list):
        raise ValueError("Both 'word' and 'word_list' must be strings or lists of strings.")
    
    lower_word = word.lower()
    return any(w.lower() == lower_word for w in word_list)

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python', 'ruby']
    print(case_insensitive_match(sample_word, sample_list))