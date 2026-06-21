import re

def validate_password(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"|\\,.<>\/?]).{8,}$'
    return bool(re.search(pattern, password))

if __name__ == '__main__':
    result = validate_password("Abcdefgh1!")
    print(result)