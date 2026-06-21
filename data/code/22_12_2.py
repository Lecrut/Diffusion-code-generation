import string
import struct
import sys

def check_password_strength(password: str) -> dict:
    if not isinstance(password, str):
        return {"valid": False, "score": 0, "reason": "Not a string"}

    length = len(password)
    if length == 0:
        return {"valid": False, "score": 0, "reason": "Empty password"}

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    lower_mask = 0
    upper_mask = 0
    digit_mask = 0
    special_mask = 0

    ascii_table = struct.unpack('256B', b'\x00' * 256)
    for i, char_code in enumerate(password.encode('ascii', 'replace')):
        if char_code == 0:
            continue
        
        if 97 <= char_code <= 122:
            has_lower = True
            lower_mask |= 1
        elif 65 <= char_code <= 90:
            has_upper = True
            upper_mask |= 1
        elif 48 <= char_code <= 57:
            has_digit = True
            digit_mask |= 1
        else:
            has_special = True
            special_mask |= 1

    score = 0
    reasons = []

    if length >= 8:
        score += 1
    else:
        reasons.append("Too short")

    if has_lower:
        score += 1
    else:
        reasons.append("No lowercase")

    if has_upper:
        score += 1
    else:
        reasons.append("No uppercase")

    if has_digit:
        score += 1
    else:
        reasons.append("No digit")

    if has_special:
        score += 2
    else:
        reasons.append("No special char")

    if length >= 12:
        score += 1
    
    if length >= 16:
        score += 1

    valid = score >= 5
    
    return {
        "valid": valid,
        "score": score,
        "reasons": reasons,
        "length": length
    }

if __name__ == '__main__':
    test_passwords = [
        "Weak",
        "Strong1",
        "V3ry$trong!Pass",
        "12345678",
        "AllLowers",
        "HasSpecial#",
        "MiXeDcAsE1!",
        "Ab1"
    ]

    results = []
    for pwd in test_passwords:
        res = check_password_strength(pwd)
        results.append(f"Password: {pwd!r} | Score: {res['score']} | Valid: {res['valid']}")

    for line in results:
        print(line)

    final_result = check_password_strength("Complex99$Pass!")
    print(f"Final Check: {final_result}")