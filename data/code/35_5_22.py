def count_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog"
    print(count_vowels(sample_string))