def count_vowels(s):
    vowels = set('aeiouAEIOU')
    total = 0
    for char in s:
        if char in vowels:
            total += 1
    return total

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(count_vowels(sample_string))