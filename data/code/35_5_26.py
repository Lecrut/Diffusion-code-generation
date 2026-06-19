def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = {vowel: 0 for vowel in vowels}
    
    for char in s:
        if char in count:
            count[char] += 1
    
    return count

if __name__ == '__main__':
    sample_string = "This is an example string with various vowels."
    result = count_vowels(sample_string)
    print(result)