def check_word_presence(words, word):
    return word.lower() in words

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    sample_word_present = "Banana"
    sample_word_absent = "grape"
    result1 = check_word_presence(sample_list, sample_word_present)
    result2 = check_word_presence(sample_list, sample_word_absent)
    print(f"Checking if '{sample_word_present}' is in the list: {result1}")
    print(f"Checking if '{sample_word_absent}' is in the list: {result2}")