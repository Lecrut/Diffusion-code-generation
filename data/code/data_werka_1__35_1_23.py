def count_vowels(s):
    vowels = set('aeiouAEIOU')
    total_vowels = 0
    for char in s:
        if char in vowels:
            total_vowels += 1
    return total_vowels

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(count_vowels(sample_string))