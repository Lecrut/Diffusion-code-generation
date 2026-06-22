VOWELS: set("aeiouAEIOU")
static_text: str = "The quick brown fox jumps over the lazy dog"

def count_vowels(text: str) -> int:
    return sum(1 for char in text if char in VOWELS)

if __name__ == '__main__':
    result: int = count_vowels(static_text)
    print(result)