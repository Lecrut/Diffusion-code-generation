def find_repeated_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    repeated = []
    for char, count in counts.items():
        if count > 1 and char not in repeated:
            repeated.append(char)
    return ''.join(repeated)

if __name__ == '__main__':
    sample = "hello world"
    print(find_repeated_characters(sample))