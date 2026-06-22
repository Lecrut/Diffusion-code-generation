def find_repeated_chars(s: str) -> list:
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    repeated = []
    for c, count in counts.items():
        if count > 1:
            repeated.append(c)
    return repeated

if __name__ == '__main__':
    sample_strings = ['hello', 'abcde', 'aabbcc', 'programming', 'python3']
    for s in sample_strings:
        result = find_repeated_chars(s)
        print(result)