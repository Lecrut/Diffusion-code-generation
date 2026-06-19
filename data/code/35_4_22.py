def count_vowels(strings):
    vowels = 'aeiouAEIOU'
    result = {}
    for string in strings:
        count = sum(1 for char in string if char in vowels)
        result[string] = count
    return result

if __name__ == '__main__':
    sample_strings = ['hello', 'world', 'python', 'programming']
    vowel_counts = count_vowels(sample_strings)
    print(vowel_counts)