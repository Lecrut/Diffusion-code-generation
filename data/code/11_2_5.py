def extract_repeated_chars(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    unique_chars = set(s)
    single_chars = {char for char in unique_chars if counts[char] == 1}
    repeated = unique_chars - single_chars
    return sorted(repeated)

if __name__ == '__main__':
    sample = "programming"
    print(extract_repeated_chars(sample))