import re

def find_target_word(words, target):
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    matches = [word for word in words if pattern.search(word)]
    return matches
if __name__ == '__main__':
    sample_words = ['Hello', 'world', 'Python', 'programming']
    target_word = 'python'
    result = find_target_word(sample_words, target_word)
    print(result)