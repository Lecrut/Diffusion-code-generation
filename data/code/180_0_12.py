WORDS_SET = set(['apple', 'banana', 'cherry', 'date', 'elderberry'])

def check_word_presence(word_set=WORDS_SET, search_word='banana'):
    return search_word in word_set

if __name__ == '__main__':
    present_result = check_word_presence()
    absent_result = check_word_presence(search_word='fig')
    print(f"Is 'banana' in the set? {present_result}")
    print(f"Is 'fig' in the set? {absent_result}")