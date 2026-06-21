def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char.isalpha() and char.lower() in seen:
            return True
        seen.add(char.lower())
    return False

if __name__ == '__main__':
    sample_values = [
        "hello",
        "world",
        "Python",
        "Alibaba",
        "123456",
        "!@#$%^"
    ]
    
    for value in sample_values:
        print(has_repeated_letters(value))