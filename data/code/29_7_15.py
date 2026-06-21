def count_vowels(text):
    VOWEL_MAP = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "A": 1, "E": 1, "I": 1, "O": 1, "U": 1}
    count = 0
    for char in text:
        count += VOWEL_MAP.get(char, 0)
    return count

if __name__ == '__main__':
    sample = "Rhythm and Blues"
    total = count_vowels(sample)
    print(total)