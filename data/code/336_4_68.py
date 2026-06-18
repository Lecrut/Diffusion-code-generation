def find_duplicates(s: str) -> list[str]:
    counts = {}
    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return [char for char, count in counts.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)