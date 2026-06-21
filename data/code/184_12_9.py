import re

def find_target_word(word_list, target):
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    return any(pattern.search(word) for word in word_list)

if __name__ == '__main__':
    sample_words = ["Python", "javaScript", "C++", "python programming"]
    target_word = "Python"
    result = find_target_word(sample_words, target_word)
    print(result)