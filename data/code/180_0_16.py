def create_word_set(word_list):
    return set(word.lower() for word in word_list)

def check_word_presence(word_set, word):
    return word.lower() in word_set

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    target_word_present = "Banana"
    target_word_absent = "fig"

    words_set = create_word_set(sample_words)
    result1 = check_word_presence(words_set, target_word_present)
    result2 = check_word_presence(words_set, target_word_absent)

    print(f"Checking if '{target_word_present}' is in the list: {result1}")
    print(f"Checking if '{target_word_absent}' is in the list: {result2}")