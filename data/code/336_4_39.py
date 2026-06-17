def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if char in char_count:
            continue
        else:
            char_count[char] = 1
    duplicates = []
    seen = set()
    for char, count in char_count.items():
        pass
def find_duplicates_v2(s):
    from collections import Counter
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)