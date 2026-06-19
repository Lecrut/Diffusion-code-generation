def find_duplicates(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return list(duplicates)

if __name__ == '__main__':
    sample_string1 = "banana"
    duplicate_chars1 = find_duplicates(sample_string1)
    print(f"Input: {sample_string1}")
    print(f"Duplicates: {duplicate_chars1}")

    sample_string2 = "mississippi"
    duplicate_chars2 = find_duplicates(sample_string2)
    print(f"Input: {sample_string2}")
    print(f"Duplicates: {duplicate_chars2}")