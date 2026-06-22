def find_repeated_chars(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    for char in s:
        if char in repeated:
            continue
    return list(repeated)

if __name__ == '__main__':
    sample = "hello world"
    result = find_repeated_chars(sample)
    print(result)