CASE_SENSITIVE = False

def case_insensitive_match(target_word, word_list):
    lower_target_word = target_word.lower() if CASE_SENSITIVE else target_word
    return any(word.lower() == lower_target_word for word in word_list)

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python', 'ruby']
    print(case_insensitive_match(sample_word, sample_list))