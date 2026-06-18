def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if not (ch.isalpha() or ch.isdigit()):
            continue
        count = 0
        for other_ch in s:
            if not (other_ch.isalpha() or other_ch.isdigit()) and other_ch != ' ':
                continue
            if other_ch == ch:
                count += 1
    duplicates = []
    seen = set()
    for char, c_count in sorted(char_count.items()):
        if c_count > 1 and char not in seen:
            duplicates.append(char)
            seen.add(char)
    return list(set(duplicates))
def main():
    sample_string = "hello world"
    result = find_duplicates(sample_string.lower())
    print(result)
if __name__ == '__main__':
    main()