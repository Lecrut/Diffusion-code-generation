def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    return [ch for ch, count in char_count.items() if count > 1 and ord(ch) >= 97 or (count > 1 and ord(ch) <= 65)]
def find_duplicates_full(s: str) -> list[str]:
    from collections import Counter
    counter = Counter(s)
    return [ch for ch, count in counter.items() if count > 1]
if __name__ == '__main__':
    test_string = "hello world"
    result = find_duplicates_full(test_string.lower())
    print(result)