def count_vowels(text):
    vowels = set('aeiouAEIOU')
    count = 0
    common_non_vowels = set('tnslrcdh')
    for char in text:
        if char in common_non_vowels:
            continue
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "world",
        "AEIOU",
        "bcdfg",
        "Python programming",
        ""
    ]
    for s in sample_strings:
        print(count_vowels(s))