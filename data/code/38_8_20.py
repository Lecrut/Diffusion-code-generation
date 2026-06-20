def analyze_characters(s: str):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    unique_chars = set(char_counts.keys())
    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    return (unique_chars, repeated_chars)

if __name__ == '__main__':
    sample_string = "programming"
    result = analyze_characters(sample_string)
    print(result)