def has_all_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    sample1 = "hello"
    sample2 = "world"
    print(has_all_unique_characters(sample1))
    print(has_all_unique_characters(sample2))