def count_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "This is a long string with various vowels and some consonants."
    print(count_vowels(sample_string))