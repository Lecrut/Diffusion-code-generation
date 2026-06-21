import re

def find_target_word(words, target):
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    return [word for word in words if pattern.search(word)]

if __name__ == '__main__':
    sample_words = ['Apple', 'banana', 'Cherry', 'apple pie']
    target_word = 'apple'
    result = find_target_word(sample_words, target_word)
    print(result)