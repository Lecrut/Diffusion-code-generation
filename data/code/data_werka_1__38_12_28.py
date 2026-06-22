def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    sample_values = ["hello", "world", "python", "unique"]
    results = {value: has_repeated_letters(value) for value in sample_values}
    print(results)