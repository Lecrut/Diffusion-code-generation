def count_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_count = {vowel: 0 for vowel in vowels}
    
    for char in s:
        if char in vowel_count:
            vowel_count[char] += 1
    
    return vowel_count

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog"
    result = count_vowels(sample_string)
    print(result)