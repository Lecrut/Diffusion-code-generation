def find_vowel_words(sentence):
    words = sentence.split()
    vowel_words = [word for word in words if any(char.lower() in 'aeiou' for char in word)]
    return vowel_words

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with many vowels and consonants."
    result = find_vowel_words(sample_sentence)
    print(result)