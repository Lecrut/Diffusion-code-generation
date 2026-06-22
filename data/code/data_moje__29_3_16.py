def count_vowels(strings):
    vowels = set('aeiouAEIOU')
    return sum(1 for s in strings for char in s if char in vowels)

if __name__ == '__main__':
    sample_strings = ["Hello", "World", "Python", "Programming", "Efficiency"]
    total_vowels = count_vowels(sample_strings)
    print(total_vowels)