def check_word_presence(word_list, word):
    word_set = set(word.lower() for word in word_list)
    return word.lower() in word_set

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    sample_word_present = "Banana"
    sample_word_absent = "grape"
    
    result1 = check_word_presence(sample_words, sample_word_present)
    result2 = check_word_presence(sample_words, sample_word_absent)
    
    print(f"Checking if '{sample_word_present}' is in list: {result1}")
    print(f"Checking if '{sample_word_absent}' is in list: {result2}")