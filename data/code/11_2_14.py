def extract_repeated_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return list(set(char for char, count in counts.items() if count > 1))

if __name__ == '__main__':
    sample_string = "programming"
    result = extract_repeated_characters(sample_string)
    print(result)