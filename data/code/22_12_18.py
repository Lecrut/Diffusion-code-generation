def evaluate_password_strength(candidate: str) -> dict:
    if not candidate:
        return {
            "length_valid": False,
            "has_upper": False,
            "has_lower": False,
            "has_digit": False,
            "has_special": False,
            "entropy_bits": 0,
            "strength_score": 0,
            "is_strong": False
        }

    length = len(candidate)
    length_valid = length >= 12

    mask_upper = 0
    mask_lower = 0
    mask_digit = 0
    mask_special = 0

    for char in candidate:
        code = ord(char)
        if 65 <= code <= 90:
            mask_upper |= (1 << (code - 65))
        elif 97 <= code <= 122:
            mask_lower |= (1 << (code - 97))
        elif 48 <= code <= 57:
            mask_digit |= (1 << (code - 48))
        else:
            mask_special |= 1

    has_upper = mask_upper != 0
    has_lower = mask_lower != 0
    has_digit = mask_digit != 0
    has_special = mask_special != 0

    active_mask = mask_upper | mask_lower | mask_digit | mask_special
    if active_mask == 0:
        charset_count = 0
    else:
        charset_count = 0
        temp_mask = active_mask
        while temp_mask > 0:
            if temp_mask & 1:
                charset_count += 1
            temp_mask >>= 1

    charset_base = 0
    if has_upper:
        charset_base += 26
    if has_lower:
        charset_base += 26
    if has_digit:
        charset_base += 10
    if has_special:
        charset_base += 33

    if charset_base == 0:
        entropy_bits = 0.0
    else:
        entropy_bits = length * (charset_base.bit_length() if charset_base < 100 else 7.0)
        
        if charset_base > 0:
            import math
            entropy_bits = length * math.log2(charset_base)

    score = 0
    if length >= 12:
        score += 20
    if length >= 16:
        score += 10
    if has_upper:
        score += 15
    if has_lower:
        score += 15
    if has_digit:
        score += 15
    if has_special:
        score += 15

    if has_upper and has_lower and has_digit and has_special:
        score += 25

    is_strong = score >= 100 and length_valid and has_upper and has_lower and has_digit and has_special

    return {
        "length_valid": length_valid,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "entropy_bits": round(entropy_bits, 2),
        "strength_score": score,
        "is_strong": is_strong
    }

if __name__ == '__main__':
    test_password = "X9#mK2$pL7&nQ1"
    result = evaluate_password_strength(test_password)
    print(result)