VOWELS_REMOVE_TABLE = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels(text):
    return text.translate(VOWELS_REMOVE_TABLE)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a sample string with vowels."
    result = remove_vowels(sample_text)
    print(result)

    another_sample = "Python Programming"
    result2 = remove_vowels(another_sample)
    print(result2)

    empty_string = ""
    result3 = remove_vowels(empty_string)
    print(result3)

    no_vowels_string = "Rhythm"
    result4 = remove_vowels(no_vowels_string)
    print(result4)

    all_vowels_string = "Aeiou AEIOU"
    result5 = remove_vowels(all_vowels_string)
    print(result5)