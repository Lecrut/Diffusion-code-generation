def is_unique(s: str) -> bool:
    if len(s) > 256:
        return False
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    print(is_unique("abcdefg"))
    print(is_unique("hello"))