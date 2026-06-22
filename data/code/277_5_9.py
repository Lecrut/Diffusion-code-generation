VOWELS = set('aeiouAEIOU')

def count_non_vowels(input_string):
    count = 0
    for char in input_string:
        if char not in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    sample_string1 = "Hello, World!"
    result1 = count_non_vowels(sample_string1)
    print(f"Non-vowel count in '{sample_string1}': {result1}")
    
    sample_string2 = "Python Programming"
    result2 = count_non_vowels(sample_string2)
    print(f"Non-vowel count in '{sample_string2}': {result2}")