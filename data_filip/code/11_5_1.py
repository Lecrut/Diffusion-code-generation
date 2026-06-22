def find_repeated_characters(s: str) -> list:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return [char for char in s if counts[char] > 1 and s.index(char) == s.index(char) and char not in [char for char in s if s.index(char) < s.index(char)]]

if __name__ == '__main__':
    text = "programming"
    result = find_repeated_characters(text)
    print(result)