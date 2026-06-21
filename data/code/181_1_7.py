import re

def find_words_with_vowels(text_list):
    vowels = r'[aeiou]'
    pattern = re.compile(vowels, re.IGNORECASE)
    words_with_vowels = set()
    
    for text in text_list:
        words = text.split()
        for word in words:
            if pattern.search(word):
                words_with_vowels.add(word.lower())
    
    return list(words_with_vowels)

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "Python programming is fun",
        "Regular expressions are powerful",
        "Vowels in a sentence"
    ]
    result = find_words_with_vowels(sample_texts)
    print(result)