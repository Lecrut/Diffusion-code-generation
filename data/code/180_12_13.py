def is_word_in_list(word, word_list):
    if not isinstance(word, str) or not all(isinstance(w, str) for w in word_list):
        raise ValueError("Word and all elements in the list must be strings")
    
    lowercased_words = set(w.lower() for w in word_list)
    return word.lower() in lowercased_words

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'c++', 'python', 'ruby']
    print(is_word_in_list(sample_word, sample_list))