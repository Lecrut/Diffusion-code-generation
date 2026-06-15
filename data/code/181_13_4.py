import re
def find_words_with_vowels(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    vowel_words = [word for word in words if any(char in 'aeiou' for char in word)]
    return vowel_words
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with some vowels and consonants."
    result = find_words_with_vowels(sample_sentence)
    print(result)