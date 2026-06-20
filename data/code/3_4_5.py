VOWELS = frozenset('aeiouAEIOU')

def strip_vowels(text):
    if not text:
        return ""
    return "".join(ch for ch in text if ch not in VOWELS)

if __name__ == '__main__':
    sample = "Hello World"
    print(strip_vowels(sample))