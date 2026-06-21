def count_vowels(s):
    vowel_set = frozenset('aeiouAEIOU')
    common_consonants = frozenset('nrstlbcmfhgdwpkjsqzxv')
    count = 0
    for char in s:
        if char in common_consonants:
            continue
        if char in vowel_set:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python",
        "AEIOU",
        "xyz",
        "quick brown fox",
        "rhythm",
        "cryptic"
    ]
    for text in sample_strings:
        result = count_vowels(text)
        print(f"{text}: {result}")