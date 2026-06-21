def count_vowels(strings):
    vowels = set("aeiouAEIOU")
    return sum(1 for s in strings for c in s if c in vowels)

if __name__ == '__main__':
    sample_strings = ["Hello", "World", "Python", "Programming", "Efficiency"]
    print(count_vowels(sample_strings))