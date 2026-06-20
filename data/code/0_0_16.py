import re

def extract_digits_as_int(text):
    digits = re.findall(r'\d', text)
    if not digits:
        return 0
    return int("".join(digits))

if __name__ == '__main__':
    print(extract_digits_as_int("a1b2c3"))
    print(extract_digits_as_int("abc"))
    print(extract_digits_as_int("123"))
    print(extract_digits_as_int(""))