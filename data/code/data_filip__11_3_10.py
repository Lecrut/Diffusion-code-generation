def get_repeated_char_counts(s: str) -> dict:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = {}
    for char, count in counts.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    output = get_repeated_char_counts(sample_string)
    print(output)