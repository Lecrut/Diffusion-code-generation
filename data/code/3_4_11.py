def strip_vowels(text):
    if not text:
        return ""
    VOWELS = frozenset("aeiouAEIOU")
    return "".join(ch for ch in text if ch not in VOWELS)

if __name__ == '__main__':
    sample_input = "Python is great"
    print(strip_vowels(sample_input))