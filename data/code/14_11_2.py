def check_uniqueness(s: str) -> bool:
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    result = check_uniqueness("abcdef")
    print(result)
    
    result2 = check_uniqueness("aabbcc")
    print(result2)