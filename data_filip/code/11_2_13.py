def extract_repeated_chars(s: str) -> str:
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return "".join(sorted(repeated, key=s.index))

if __name__ == '__main__':
    sample_input = "programming"
    result = extract_repeated_chars(sample_input)
    print(result)