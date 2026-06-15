import re
def find_vowel_words(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    vowel_words = [word for word in words if re.search(r'[aeiou]', word)]
    return vowel_words
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with several vowels present."
    result = find_vowel_words(sample_sentence)
    print(result)