def filter_repeated_chars(text: str) -> str:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    result = []
    seen = set()
    for char in text:
        if counts[char] > 1 and char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "programming"
    output = filter_repeated_chars(sample_input)
    print(output)