import re

def find_word_in_list(word, string_list):
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    return [s for s in string_list if pattern.search(s)]

if __name__ == '__main__':
    target_word = 'example'
    sample_strings = ['Example sentence.', 'Another example here.', 'No match here.']
    print(find_word_in_list(target_word, sample_strings))