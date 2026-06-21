VOWELS = {"a", "e", "i", "o", "u"}

def count_vowels(text: str) -> int:
    count = 0
    for char in text.lower():
        if char in VOWELS:
            count += 1
    return count

if __name__ == "__main__":
    sample_text = "Hello World! This is an optimized Python script for counting vowels efficiently."
    result = count_vowels(sample_text)
    print(result)