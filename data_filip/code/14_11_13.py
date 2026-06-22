def has_unique_characters(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    print(has_unique_characters("abc"))
    print(has_unique_characters("aba"))