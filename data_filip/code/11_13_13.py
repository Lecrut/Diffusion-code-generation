def get_repeated_characters(text: str) -> list:
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return sorted(repeated)

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_characters(sample_string)
    print(result)