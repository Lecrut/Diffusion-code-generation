def extract_repeated_characters(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return [char for char in text if char in repeated]
if __name__ == '__main__':
    sample_string = 'programming'
    result = extract_repeated_characters(sample_string)
    print(result)