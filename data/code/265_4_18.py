def extract_vowels_reverse(phrase):
    vowels = "aeiouAEIOU"
    return ''.join(filter(lambda x: x in vowels, phrase[::-1]))

if __name__ == '__main__':
    sample_phrase = "Programming is fun!"
    result = extract_vowels_reverse(sample_phrase)
    print(result)