def count_vowels_optimized(text):
    vowel_map = str.maketrans({
        'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
        'A': 'A', 'E': 'E', 'I': 'I', 'O': 'O', 'U': 'U'
    })
    valid_vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in valid_vowels:
            count += 1
    return count

if __name__ == '__main__':
    large_string = "The quick brown fox jumps over the lazy dog. All work and no play makes Jack a dull boy. She sells seashells by the seashore." * 10000
    result = count_vowels_optimized(large_string)
    print(result)