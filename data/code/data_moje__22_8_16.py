import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "letmein",
    "welcome", "shadow", "superman", "michael", "football", "cheese", "princess",
    "access", "charlie", "maggie", "passw0rd", "login", "admin", "guest", "root"
}

def validate_password_strength(password: str) -> dict:
    results = {
        "length_ok": False,
        "uppercase_ok": False,
        "lowercase_ok": False,
        "digit_ok": False,
        "special_ok": False,
        "not_common": False,
        "is_valid": False
    }

    if len(password) >= 8:
        results["length_ok"] = True

    if re.search(r'[A-Z]', password):
        results["uppercase_ok"] = True

    if re.search(r'[a-z]', password):
        results["lowercase_ok"] = True

    if re.search(r'\d', password):
        results["digit_ok"] = True

    if re.search(r'[^A-Za-z0-9]', password):
        results["special_ok"] = True

    if password.lower() not in COMMON_PASSWORDS:
        results["not_common"] = True

    all_criteria_met = all([
        results["length_ok"],
        results["uppercase_ok"],
        results["lowercase_ok"],
        results["digit_ok"],
        results["special_ok"],
        results["not_common"]
    ])
    results["is_valid"] = all_criteria_met

    return results

if __name__ == '__main__':
    test_password = "MyP@ssw0rd!"
    result = validate_password_strength(test_password)
    print(result)