def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    sample_string = "hello"
    print(has_repeated_letters(sample_string))