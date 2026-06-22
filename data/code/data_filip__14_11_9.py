def has_unique_characters(input_str):
    if not input_str:
        return True
    visited = set()
    for char in input_str:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    print(has_unique_characters('abcdef'))
    print(has_unique_characters('abca'))