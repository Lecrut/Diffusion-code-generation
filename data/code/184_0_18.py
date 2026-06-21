def word_exists(word_list, target_word):
    word_set = set(word_list)
    return target_word in word_set

if __name__ == '__main__':
    sample_words = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon"
    ]
    target = "banana"
    
    if word_exists(sample_words, target):
        print(f"The word '{target}' exists in the list.")
    else:
        print(f"The word '{target}' does not exist in the list.")