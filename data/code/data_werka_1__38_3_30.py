def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    sample_values = ["hello", "world", "python", "unique"]
    for value in sample_values:
        print(f"'{value}' has repeated letters: {has_repeated_letters(value)}")