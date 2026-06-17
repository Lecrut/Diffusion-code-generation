def has_unique_chars(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_cases = ["hello", "abcdefg", "aabb"]
    for tc in test_cases:
        print(f"{tc}: {has_unique_chars(tc)}")