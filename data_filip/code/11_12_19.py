def filter_duplicate_chars(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return ''.join(duplicates)

if __name__ == '__main__':
    sample = "hello world"
    result = filter_duplicate_chars(sample)
    print(result)