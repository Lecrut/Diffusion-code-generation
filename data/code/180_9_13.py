SUBSTRING_CHECK = "substring"

def is_target_word_present(word_list, target):
    if not word_list:
        return False
    if not isinstance(target, str):
        raise TypeError("Target must be a string")
    return target in word_list

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry"]
    target_word1 = "banana"
    target_word2 = 123
    print(f"Is '{target_word1}' present? {is_target_word_present(sample_words, target_word1)}")
    try:
        print(f"Is '{target_word2}' present? {is_target_word_present(sample_words, target_word2)}")
    except TypeError as e:
        print(e)