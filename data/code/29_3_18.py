def count_vowels(strings):
    return sum(len([c for c in s if c.lower() in 'aeiou']) for s in strings)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    print(count_vowels(sample_strings))