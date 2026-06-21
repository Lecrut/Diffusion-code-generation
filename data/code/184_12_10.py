import re

def find_target_word(word_list, target):
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    return any(pattern.search(word) for word in word_list)

if __name__ == '__main__':
    sample_words = ["Hello", "world", "Python", "programming"]
    target_word = "python"
    result = find_target_word(sample_words, target_word)
    print(result)