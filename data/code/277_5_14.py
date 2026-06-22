def count_non_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_non_vowels(sample_string)
    print(f"Number of non-vowel characters in '{sample_string}': {result}")