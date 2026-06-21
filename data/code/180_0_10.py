def check_word_presence(words, target):
    return target in words

if __name__ == '__main__':
    sample_words = {"apple", "banana", "cherry"}
    sample_target_present = "banana"
    sample_target_absent = "grape"

    result1 = check_word_presence(sample_words, sample_target_present)
    result2 = check_word_presence(sample_words, sample_target_absent)

    print(f"Checking if '{sample_target_present}' is in the set: {result1}")
    print(f"Checking if '{sample_target_absent}' is in the set: {result2}")