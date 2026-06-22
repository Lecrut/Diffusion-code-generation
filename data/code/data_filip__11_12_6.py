def filter_duplicated_chars(text: str) -> list:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "programming"
    result = filter_duplicated_chars(sample_text)
    print(result)