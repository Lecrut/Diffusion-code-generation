def find_repeated_chars(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(repeated))

if __name__ == '__main__':
    sample = "programming"
    print(find_repeated_chars(sample))