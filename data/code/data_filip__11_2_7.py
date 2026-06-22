def get_repeated_chars(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(repeated))

if __name__ == '__main__':
    sample_text = "programming"
    result = get_repeated_chars(sample_text)
    print(result)