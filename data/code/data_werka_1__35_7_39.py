def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char in vowels)

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    print(count_vowels(sample_string))