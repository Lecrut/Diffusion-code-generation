import re

def extract_words_with_vowels(texts):
    if not all(isinstance(text, str) for text in texts):
        raise ValueError("All elements in the list must be strings.")
    
    vowel_pattern = re.compile(r'\b\w*[aeiouAEIOU]\w*\b', re.IGNORECASE)
    words_with_vowels = set(word.lower() for text in texts for word in re.findall(vowel_pattern, text))
    return list(words_with_vowels)

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "AEIOUaeiou",
        "Rhythm",
        "Programming is Fun"
    ]
    result = extract_words_with_vowels(sample_texts)
    print(f"Words with vowels: {result}")