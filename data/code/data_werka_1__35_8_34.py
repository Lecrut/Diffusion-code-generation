def count_vowels(text):
    vowel_map = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in text.lower():
        if char in vowel_map:
            vowel_map[char] += 1
    return sum(vowel_map.values())

if __name__ == '__main__':
    sample_text1 = "Hello World! 123"
    sample_text2 = "Programming is fun, how are you?"
    sample_text3 = "Rhythm myth"
    sample_text4 = "AEIOUaeiou123"
    result1 = count_vowels(sample_text1)
    result2 = count_vowels(sample_text2)
    result3 = count_vowels(sample_text3)
    result4 = count_vowels(sample_text4)
    print(result1)
    print(result2)