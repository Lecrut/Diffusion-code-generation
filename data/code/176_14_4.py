import re
def find_all_words(text):
    words = set()
    for char in text:
        if char.isalpha():
            words.add(char.lower())
    return list(words)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with some punctuation."
    sample_string2 = "Python programming is fun. Is it efficient?"
    sample_string3 = "A B C dE fG"
    print(f"Sample 1: {find_all_words(sample_string1)}")
    print(f"Sample 2: {find_all_words(sample_string2)}")
    print(f"Sample 3: {find_all_words(sample_string3)}")