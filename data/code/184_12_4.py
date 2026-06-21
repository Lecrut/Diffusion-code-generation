import re

def find_target_word(words, target):
    if not isinstance(target, str) or not all(isinstance(word, str) for word in words):
        raise ValueError("Target must be a string and words must be a list of strings.")
    
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    return [word for word in words if pattern.search(word)]

if __name__ == '__main__':
    sample_words = ['Apple', 'banana', 'Cherry', 'apple pie']
    target_word = 'apple'
    result = find_target_word(sample_words, target_word)
    print(result)