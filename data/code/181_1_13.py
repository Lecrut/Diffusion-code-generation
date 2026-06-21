import re

def find_words_with_vowels(text_list):
    vowels = r'[aeiouAEIOU]'
    pattern = r'\b\w*' + vowels + r'\w*\b'
    words_with_vowels = set()
    
    for text in text_list:
        matches = re.findall(pattern, text)
        words_with_vowels.update(matches)
    
    return list(words_with_vowels)

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "Python programming is fun",
        "A quick brown fox jumps over the lazy dog"
    ]
    result = find_words_with_vowels(sample_texts)
    print(result)