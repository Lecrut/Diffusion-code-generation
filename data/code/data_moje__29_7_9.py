def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    sample_strings = ["Hello World", "Python Programming", "AEIOU aeiou", "No vowels here"]
    for sample in sample_strings:
        print(count_vowels(sample))