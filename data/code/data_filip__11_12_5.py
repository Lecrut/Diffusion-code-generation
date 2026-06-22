def filter_non_unique_chars(s: str) -> str:
    if len(s) <= 1:
        return ""
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = []
    for char in s:
        if counts[char] > 1:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "abcaadefgg"
    filtered_string = filter_non_unique_chars(sample_string)
    print(filtered_string)