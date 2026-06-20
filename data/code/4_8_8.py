VOWELS = frozenset("aeiouAEIOU")
NON_ALPHABET = frozenset(" -.,!?;:'\"\n\r\t")

def count_consonants(text: str) -> int:
    return sum(1 for char in text if char.isalpha() and char not in VOWELS and char not in NON_ALPHABET)

if __name__ == "__main__":
    text = "Hello, World! 123."
    result = count_consonants(text)
    print(result)