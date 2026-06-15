import sys
def check_word_presence(text, word):
    return word in text.lower()
if __name__ == '__main__':
    sample_string = "This is a Test string containing the word test."
    sample_word_present = "Test"
    sample_word_absent = "word"
    result1 = check_word_presence(sample_string, sample_word_present)
    result2 = check_word_presence(sample_string, sample_word_absent)
    print(f"Checking if '{sample_word_present}' is in '{sample_string}': {result1}")
    print(f"Checking if '{sample_word_absent}' is in '{sample_string}': {result2}")