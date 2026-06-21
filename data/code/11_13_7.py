def get_repeated_characters(text: str) -> list[str]:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return sorted([char for char, count in counts.items() if count > 1])

if __name__ == '__main__':
    sample_text: str = "programming"
    result: list[str] = get_repeated_characters(sample_text)
    print(result)