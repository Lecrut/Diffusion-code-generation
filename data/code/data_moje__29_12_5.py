def count_vowels():
    text = "The quick brown fox jumps over the lazy dog"
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    print(count_vowels())