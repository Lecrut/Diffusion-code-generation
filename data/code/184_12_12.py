import re

def find_target_word(word_list, target):
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    return [word for word in word_list if pattern.search(word)]
if __name__ == '__main__':
    sample_words = ['Apple', 'banana', 'Cherry', 'apple pie', 'Banana Bread']
    target_word = 'apple'
    result = find_target_word(sample_words, target_word)
    print(result)