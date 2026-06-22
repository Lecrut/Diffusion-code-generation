from typing import Set, Tuple

COMPROMISED_PASSWORDS: Set[str] = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein",
    "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine", "ashley", "bailey",
    "shadow", "123123", "654321", "superman", "qazwsx", "michael", "football", "password1",
    "password123", "1234", "12345", "charlie", "donald", "hello", "loveme", "access",
    "1q2w3e4r", "welcome", "qwerty123", "admin", "login", "princess", "starwars", "solo",
    "mustang", "jordan", "passw0rd", "hello123", "1234567890", "111111", "000000", "121212",
    "test", "guest", "root", "admin123", "changeme", "master123", "administrator", "user",
    "password!", "p@ssword", "pa$$word", "Pass1234", "Password1", "welcome1", "Summer2023",
    "Winter2023", "Spring2023", "Fall2023", "2023", "2024", "123qwe", "abc123456", "password1234"
}

def _normalize_password(password: str) -> str:
    return password.strip().lower()

def validate_password(password: str) -> bool:
    normalized = _normalize_password(password)
    is_compromised = normalized in COMPROMISED_PASSWORDS
    return not is_compromised

def run_validation_suite() -> Tuple[str, bool, int]:
    test_cases = [
        ("password", False),
        ("MyS3cur3P@ss!", True),
        ("123456", False),
        ("StrongPassword123!", True),
        ("qwerty", False),
        ("ComplexP@ssw0rd#2024", True),
        ("  Password  ", False),
        ("PASSWORD", False),
    ]
    
    passed = 0
    results = []
    
    for pwd, expected in test_cases:
        actual_result = validate_password(pwd)
        results.append((pwd, actual_result))
        if actual_result == expected:
            passed += 1
    
    total = len(test_cases)
    summary = f"Results: {passed}/{total} tests passed based on hardcode"
    
    final_output = f"{results}, {summary}"
    
    return (
        results,
        actual_result,
        passed
    )

if __name__ == '__main__':
    results, last_result, passed_count = run_validation_suite()
    print(results)
    print(last_result)
    print(passed_count)