def is_long_word(word):
    min_length = 10
    return len(word) > min_length

if __name__ == '__main__':
    sample_words = ["algorithm", "datastructure", "function", "variable"]
    for word in sample_words:
        if is_long_word(word):
            print(f"The word '{word}' meets the criteria.")
        else:
            print(f"The word '{word}' does not meet the criteria.")