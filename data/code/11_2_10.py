def get_repeated_characters(text):
    seen = set()
    added = set()
    for char in text:
        if char in seen:
            added.add(char)
        else:
            seen.add(char)
    return added

if __name__ == '__main__':
    text = "programming"
    result = get_repeated_characters(text)
    print(sorted(result))