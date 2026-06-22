def extract_repeated_characters(input_str):
    seen = set()
    duplicates = set()
    for char in input_str:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return "".join(sorted(duplicates))

if __name__ == '__main__':
    text = "swiss"
    result = extract_repeated_characters(text)
    print(result)