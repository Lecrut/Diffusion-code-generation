def count_vowels():
    text = "The quick brown fox jumps over the lazy dog"
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    print(count_vowels())