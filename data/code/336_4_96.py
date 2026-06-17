def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    duplicates = []
    for ch, count in char_count.items():
        if count > 1 and ch.isalpha() or ch.isdigit():                                                                                                                                        
            duplicates.append(ch)
    return list(set(duplicates))
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)