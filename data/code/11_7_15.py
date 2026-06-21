def find_duplicates(s):
    seen = set()
    duplicates = []
    for char in s:
        if char in seen:
            if char not in duplicates:
                duplicates.append(char)
        else:
            seen.add(char)
    return ''.join(duplicates)

if __name__ == '__main__':
    result = find_duplicates("programming")
    print(result)