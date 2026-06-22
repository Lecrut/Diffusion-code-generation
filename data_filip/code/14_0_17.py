def all_chars_unique(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

if __name__ == '__main__':
    test_str = "unique!"
    print(all_chars_unique(test_str))