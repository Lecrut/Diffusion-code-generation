def filter_unique_characters(s: str) -> list:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = []
    for char in s:
        if counts[char] > 1 and char not in result:
            result.append(char)
    return result

if __name__ == '__main__':
    sample_string = "programming"
    print(filter_unique_characters(sample_string))