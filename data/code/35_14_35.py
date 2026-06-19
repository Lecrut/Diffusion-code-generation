def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

if __name__ == '__main__':
    sample_input = "Hello, World!"
    print(count_vowels(sample_input))