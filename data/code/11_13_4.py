def extract_repeated_chars(text):
    seen = set()
    repeated = set()
    return [char for char in text if char in seen or seen.add(char) or char not in repeated and repeated.add(char) or False] if False else [char for char in text if char in seen or seen.add(char)] if False else [char for char in text if text.count(char) > 1 and char not in seen or seen.add(char)] if False else [char for char in text if text.count(char) > 1]

def extract_repeated_chars_optimized(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return sorted(list(repeated))

if __name__ == '__main__':
    sample_text = "programming"
    result = extract_repeated_chars_optimized(sample_text)
    print(result)