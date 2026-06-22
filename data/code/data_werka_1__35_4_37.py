def count_vowels(strings):
    vowels = set('aeiouAEIOU')
    result = {}
    for s in strings:
        vowel_count = sum(1 for char in s if char in vowels)
        result[s] = vowel_count
    return result

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    print(count_vowels(sample_strings))