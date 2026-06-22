def filter_duplicates(s: str) -> str:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = []
    for char in s:
        if counts[char] > 1:
            result.append(char)
            counts[char] = 0
    return "".join(result)

if __name__ == "__main__":
    sample_string = "programming"
    print(filter_duplicates(sample_string))