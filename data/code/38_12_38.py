def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char.isalpha() and char.lower() in seen:
            return True
        seen.add(char.lower())
    return False
if __name__ == '__main__':
    print(has_repeated_letters('hello'))
    print(has_repeated_letters('world'))
    print(has_repeated_letters('Alibaba'))
    print(has_repeated_letters('Python'))