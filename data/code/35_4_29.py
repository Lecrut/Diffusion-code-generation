def count_vowels(strings):
    vowels = 'aeiouAEIOU'
    result = {}
    for string in strings:
        vowel_count = sum(1 for char in string if char in vowels)
        result[string] = vowel_count
    return result

if __name__ == '__main__':
    sample_values = ['hello', 'world', 'python', 'programming']
    print(count_vowels(sample_values))