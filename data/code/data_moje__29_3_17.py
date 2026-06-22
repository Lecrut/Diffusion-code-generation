def count_total_vowels(strings):
    vowels = "aeiouAEIOU"
    return sum(1 for s in strings for char in s if char in vowels)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "Python", "programming", "list", "comprehension"]
    result = count_total_vowels(sample_strings)
    print(result)