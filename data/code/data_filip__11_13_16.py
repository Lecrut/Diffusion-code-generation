def get_repeated_chars(text: str) -> str:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    repeated = [char for char, count in counts.items() if count > 1]
    seen = set()
    result = [char for char in text if char in repeated and char not in seen and not seen.add(char)]
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "abracadabra"
    result = get_repeated_chars(sample_text)
    print(result)