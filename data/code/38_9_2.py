def analyze_string(s):
    unique_chars = set(s)
    repeated_chars = []
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            repeated_chars.append(char)
    return (unique_chars, repeated_chars)
if __name__ == '__main__':
    sample_string = "hello world"
    result = analyze_string(sample_string)
    print(result)