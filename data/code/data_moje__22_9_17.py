import unicodedata

MAX_CODE_POINT = 0x10FFFF
SURROGATE_START = 0xD800
SURROGATE_END = 0xDFFF

def is_unicode_safe(char):
    code = ord(char)
    return code <= MAX_CODE_POINT and not (SURROGATE_START <= code <= SURROGATE_END)

def get_category_flags(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for char in password:
        cat = unicodedata.category(char)
        if cat.startswith('Lu'):
            has_upper = True
        elif cat.startswith('Ll'):
            has_lower = True
        elif cat.startswith('Nd'):
            has_digit = True
        elif not cat.startswith('L') and not cat.startswith('N') and not cat.startswith('Z'):
            has_symbol = True
    return has_upper, has_lower, has_digit, has_symbol

def validate_password_strength(password):
    if not isinstance(password, str):
        return False
    if not all(is_unicode_safe(c) for c in password):
        return False
    u, l, d, s = get_category_flags(password)
    count = sum([u, l, d, s])
    return count >= 3

class PasswordCheck:
    def __init__(self, pwd):
        self.result = validate_password_strength(pwd)

if __name__ == '__main__':
    samples = ["Abc123!", "simple", "12345", "A_b_c!"]
    for s in samples:
        obj = PasswordCheck(s)
        print(obj.result)