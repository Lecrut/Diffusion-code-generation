def count_vowels(s):
    vowels = frozenset('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    sample_string = "This is a unique test string with various vowels."
    print(count_vowels(sample_string))