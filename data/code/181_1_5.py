import re

def find_words_with_vowels(text_list):
    vowel_pattern = r'\b\w*[aeiouAEIOU]\w*\b'
    words_with_vowels = set()
    
    for text in text_list:
        matches = re.findall(vowel_pattern, text)
        words_with_vowels.update(matches)
    
    return list(words_with_vowels)

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "Python programming is fun",
        "Regular expressions are powerful",
        "Vowels include a, e, i, o, u"
    ]
    result = find_words_with_vowels(sample_texts)
    print(result)