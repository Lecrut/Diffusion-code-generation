def find_repeated_characters(s):
    counts = {}
    repeated = []
    seen_repeated = set()
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        if counts[char] == 2:
            repeated.append(char)
            seen_repeated.add(char)
    return repeated

if __name__ == '__main__':
    test_string = "programming"
    result = find_repeated_characters(test_string)
    print(result)