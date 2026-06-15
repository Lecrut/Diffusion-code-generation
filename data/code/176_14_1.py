import re
def find_all_words(text):
    words = set()
    for char in text:
        if char.isalpha():
            words.add(char.lower())
    return list(words)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with mixed cases."
    sample_string2 = "Python programming is fun; let's see it."
    sample_string3 = "A B C. 123!"
    result1 = find_all_words(sample_string1)
    print(f"'{sample_string1}' -> {result1}")
    result2 = find_all_words(sample_string2)
    print(f"'{sample_string2}' -> {result2}")
    result3 = find_all_words(sample_string3)
    print(f"'{sample_string3}' -> {result3}")