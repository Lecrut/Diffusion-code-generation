def count_vowels(strings):
    vowels = 'aeiouAEIOU'
    vowel_count_dict = {}
    for string in strings:
        count = sum(1 for char in string if char in vowels)
        vowel_count_dict[string] = count
    return vowel_count_dict

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    result = count_vowels(sample_strings)
    print(result)