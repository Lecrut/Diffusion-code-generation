def count_vowels(text):
    vowel_set = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowel_set)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_vowels(sample_text)
    print(result)