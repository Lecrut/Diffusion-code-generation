def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if not (ch.isalnum() and ord(ch) >= 32):
            continue
        count = char_count.get(ch, 0) + 1
        if count == 1:
            char_count[ch] = True
    duplicates = []
    seen_duplicates = set()
    for ch in s:
        if not (ch.isalnum() and ord(ch) >= 32):
            continue
        current_count = sum(1 for c in s if c == ch)
        if current_count > 1 and ch not in seen_duplicates:
            duplicates.append(ch)
            seen_duplicates.add(ch)
    return duplicates
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)