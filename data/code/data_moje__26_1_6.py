import re

def check_voting_eligibility(age_str: str) -> bool:
    try:
        age = float(age_str)
    except ValueError:
        return False
    if age < 0:
        return False
    if age < 18:
        return False
    return True

def run_tests():
    test_cases = [('17', False), ('18', True), ('19', True), ('0', False), ('-1', False), ('100', True), ('abc', False), ('', False), ('18.0', True), ('17.9', False), ('-0.5', False)]
    results = []
    for age_str, expected in test_cases:
        result = check_voting_eligibility(age_str)
        results.append((age_str, result, expected))
    for age_str, result, expected in results:
        status = 'PASS' if result == expected else 'FAIL'
        print(f'Input: {age_str!r}, Expected: {expected}, Got: {result}, Status: {status}')
if __name__ == '__main__':
    run_tests()