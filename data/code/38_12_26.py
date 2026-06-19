def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_string1 = 'hello'
    sample_string2 = 'world'
    print(has_repeated_letters(sample_string1))
    print(has_repeated_letters(sample_string2))