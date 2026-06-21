import re

def validate_password_complexity(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]).{8,}$'
    return bool(re.match(pattern, password))

if __name__ == '__main__':
    result = validate_password_complexity("Abc12345!")
    print(result)