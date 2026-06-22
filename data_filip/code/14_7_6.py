def is_unique(s):
    if len(s) > 256:
        return False
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample = "abcdefg"
    result = is_unique(sample)
    print(result)