import re

def find_target_word(strings, target):
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    return [s for s in strings if pattern.search(s)]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python is great", "hello again"]
    target_word = "hello"
    result = find_target_word(sample_strings, target_word)
    print(result)