def count_vowels(s: str) -> int:
    count = 0
    vowels = set('aeiouAEIOU')
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = ["hello", "Python", "AEIOU", "xyz", "quick brown fox"]
    for text in sample_strings:
        print(f"{text}: {count_vowels(text)}")