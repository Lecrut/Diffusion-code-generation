def count_vowels(strings):
    vowels = set("aeiouAEIOU")
    total = sum(1 for s in strings for char in s if char in vowels)
    return total

if __name__ == '__main__':
    sample_strings = ["hello", "world", "Python", "programming"]
    result = count_vowels(sample_strings)
    print(result)