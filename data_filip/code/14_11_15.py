def is_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    sample_string = "python"
    result = is_unique_chars(sample_string)
    print(result)