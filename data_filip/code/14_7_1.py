def is_unique(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample = "hello"
    result = is_unique(sample)
    print(result)