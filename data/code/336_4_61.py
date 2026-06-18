def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 1
        else:
            char_count[ch] += 1
    duplicates = []
    for ch, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (count > 1):
            is_duplicate = False
            for d in duplicates:
                if d[0] == ch:
                    is_duplicate = True
                    break
            if not is_duplicate and count > 1:
                duplicates.append((ch, count))
    return [duplicates[i][0].lower() for i in range(len(duplicates))]
def main():
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)
if __name__ == '__main__':
    main()