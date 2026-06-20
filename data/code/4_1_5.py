import re

def count_consonants(word):
    if not isinstance(word, str):
        return 0
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', cleaned_word)
    return len(consonants)

if __name__ == '__main__':
    sample_words = ["Hello, World!", "Python3.11", "Rhythm!!", "AEIOU", "BcD", "!!!", ""]
    for w in sample_words:
        result = count_consonants(w)
        print(f"Word: {w}, Consonant Count: {result}")