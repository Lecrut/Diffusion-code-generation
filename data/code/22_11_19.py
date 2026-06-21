import re

def is_valid_password(password: str) -> bool:
    return bool(re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"|,.<>\/?]).{8,}$', password))

if __name__ == '__main__':
    test_passwords = [
        "Ab1!xxxx",
        "short",
        "alllowercase1!",
        "ALLUPPERCASE1!",
        "NoDigitsHere!",
        "NoSpecial1Ab",
        "Perfect1Pass!"
    ]
    results = [(p, is_valid_password(p)) for p in test_passwords]
    print(results)