import re

def count_consonants(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
    return len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', cleaned_word, re.IGNORECASE))

if __name__ == '__main__':
    sample_words = ["Hello, World!", "Python3.9", "123!@#", "AEIOU", "sky", "Zx9#bV"]
    for w in sample_words:
        result = count_consonants(w)
        print(f"Input: {w} -> Consonants: {result}")