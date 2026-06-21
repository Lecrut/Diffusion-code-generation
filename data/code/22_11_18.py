import re

def validate_password(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]).{8,}$'
    return bool(re.match(pattern, password))

if __name__ == '__main__':
    print(validate_password("Strong1!"))
    print(validate_password("weak"))
    print(validate_password("NoSpecial1"))
    print(validate_password("nospecial1!"))
    print(validate_password("NOLOWER1!"))
    print(validate_password("Sh0rt!"))
    print(validate_password("ValidP@ss1"))