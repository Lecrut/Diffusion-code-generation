def count_vowels(text: str) -> int:
    if not text:
        return 0
    count: int = 0
    for c in text:
        if c in 'aeiouAEIOU':
            count += 1
    return count

if __name__ == '__main__':
    sample_text: str = "Programming is fun"
    print(count_vowels(sample_text))