def get_repeated_chars(text: str) -> set:
    seen = set()
    repeated = {char for char in text if char in seen or seen.add(char) is None or char in seen}
    seen.clear()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return repeated

if __name__ == '__main__':
    sample_text = 'hello world'
    result = get_repeated_chars(sample_text)
    print(sorted(result))