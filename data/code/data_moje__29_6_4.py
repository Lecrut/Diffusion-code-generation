def count_vowels(s):
    vowels = set('aeiouAEIOU')
    common_non_vowels = set('ntslrh')
    count = 0
    for char in s:
        if char in common_non_vowels:
            continue
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "world",
        "Python programming",
        "AEIOU",
        "bcdfg",
        ""
    ]
    for s in sample_strings:
        print(count_vowels(s))