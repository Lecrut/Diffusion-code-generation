def count_vowels(strings):
    vowels = 'aeiouAEIOU'
    vowel_counts = {s: sum(1 for char in s if char in vowels) for s in strings}
    return vowel_counts

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    result = count_vowels(sample_strings)
    print(result)