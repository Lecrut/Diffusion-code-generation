import re

def compile_pattern(target):
    return re.compile(re.escape(target), re.IGNORECASE)

def find_target_word(words, target):
    pattern = compile_pattern(target)
    return any(pattern.search(word) for word in words)

if __name__ == '__main__':
    sample_words = ["Hello", "world", "Python", "programming"]
    target_word = "python"
    result = find_target_word(sample_words, target_word)
    print(result)