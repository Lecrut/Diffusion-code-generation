def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 0
        char_count[c] += 1
    duplicates = []
    for c, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (len(c) != 1):                                                                                                                                                                                                                                         
            pass
    for c in char_count:
        if count > 1 and len(c) == 1:                                                                                                                                                                                                                                                                       
            duplicates.append(c)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)