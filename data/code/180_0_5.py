import sys
def check_word_presence(text, word):
    return word in text.lower()
if __name__ == '__main__':
    sample_string = "The quick Brown fox jumps over the lazy dog."
    sample_word_present = "Fox"
    sample_word_absent = "cat"
    result1 = check_word_presence(sample_string, sample_word_present)
    print(f"'{sample_word_present}' in '{sample_string}': {result1}")
    result2 = check_word_presence(sample_string, sample_word_absent)
    print(f"'{sample_word_absent}' in '{sample_string}': {result2}")