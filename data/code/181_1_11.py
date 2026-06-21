import re

def find_words_with_vowels(words):
    pattern = r'\b\w*[aeiouAEIOU]\w*\b'
    return list(set(word for word in words if re.search(pattern, word)))

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "Python programming is fun",
        "Regular expressions are powerful",
        "Vowels include a, e, i, o, u"
    ]
    result = find_words_with_vowels(sample_texts)
    print(result)