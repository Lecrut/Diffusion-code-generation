VOWEL_SET = frozenset("aeiouAEIOU")

def count_vowels(text: str) -> int:
    count = 0
    for char in text:
        if char in VOWEL_SET:
            count += 1
    return count

if __name__ == "__main__":
    samples = ["Hello World", "AEIOU", "bcdfg", "Python Programming", ""]
    for s in samples:
        print(count_vowels(s))