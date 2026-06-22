def find_repeated_chars(text):
    seen = set()
    duplicates = set()
    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return "".join(sorted(duplicates))

if __name__ == '__main__':
    result = find_repeated_chars("programming")
    print(result)