def run_length_encode(digits: str) -> list[str]:
    if not digits:
        return []
    
    result = []
    current_digit = digits[0]
    count = 1
    
    for i in range(1, len(digits)):
        digit = digits[i]
        if digit == current_digit:
            count += 1
        else:
            result.append(f"{count}{current_digit}")
            current_digit = digit
            count = 1
    result.append(f"{count}{current_digit}")
    
    return result

if __name__ == '__main__':
    sample_digits = "11222333334"
    encoded = run_length_encode(sample_digits)
    print(encoded)