import re

def validate_password_complexity(password: str) -> bool:
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]).{8,}$')
    return bool(pattern.search(password))

if __name__ == '__main__':
    samples = ["Password1!", "short1A!", "alllowercase1!", "NOdigit!Here", "Has1Special#"]
    for pwd in samples:
        print(validate_password_complexity(pwd))