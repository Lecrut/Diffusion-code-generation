def count_total_vowels(strings):
    vowels = set("aeiouAEIOU")
    total = sum(1 for s in strings for char in s if char in vowels)
    return total

if __name__ == '__main__':
    sample_strings = ["Hello", "World", "Python", "Programming"]
    result = count_total_vowels(sample_strings)
    print(result)