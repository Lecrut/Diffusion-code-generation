def is_valid_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

def count_consonants(text):
    is_valid_input(text)
    vowels = frozenset("aeiou")
    total = 0
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha() and lower_char not in vowels:
            total += 1
    return total

if __name__ == '__main__':
    test_cases = [
        "The Quick Brown Fox",
        "aEiOu",
        "123xyz!@#",
        "",
        "BCDFGHJKLMNPQRSTVWXYZ"
    ]
    for case in test_cases:
        print(count_consonants(case))