def analyze_string(s):
    unique_chars = set(s)
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    repeated_chars = [char for char, count in counts.items() if count > 1]
    return (unique_chars, repeated_chars)
if __name__ == '__main__':
    sample_string = "hello world"
    result = analyze_string(sample_string)
    print(result)