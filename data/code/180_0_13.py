def check_word_presence(words_set, word):
    return word.lower() in words_set

if __name__ == '__main__':
    sample_words = set(["apple", "banana", "cherry", "date"])
    sample_word_present = "Banana"
    sample_word_absent = "grape"
    
    result1 = check_word_presence(sample_words, sample_word_present)
    result2 = check_word_presence(sample_words, sample_word_absent)
    
    print(f"Checking if '{sample_word_present}' is in the set: {result1}")
    print(f"Checking if '{sample_word_absent}' is in the set: {result2}")