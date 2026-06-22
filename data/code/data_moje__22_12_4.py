import sys
import time

def check_password_strength(password):
    if not password:
        return False

    length = len(password)
    if length < 12:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')

    for char in password:
        code = ord(char)

        if 65 <= code <= 90:
            has_upper = True
        elif 97 <= code <= 122:
            has_lower = True
        elif 48 <= code <= 57:
            has_digit = True
        elif char in special_chars:
            has_special = True

        if has_upper and has_lower and has_digit and has_special:
            return True

    return False

def run_performance_test():
    passwords = [
        "Weak123",
        "StrongP@ssw0rd!",
        "AnotherS3cur3#Password",
        "Short1!",
        "ALLUPPERCASE123!",
        "alllowercase123!",
        "NoSpecialChars123",
        "N0Digits!Abc",
        "1234567890!@",
        "MixedCase123!@#",
    ]

    start_time = time.perf_counter()
    results = []
    for pwd in passwords:
        is_strong = check_password_strength(pwd)
        results.append(is_strong)
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    return results, execution_time

if __name__ == '__main__':
    results, exec_time = run_performance_test()
    for result in results:
        print(result)
    print(exec_time)