import re

def is_valid_us_phone(number: str) -> bool:
    pattern = r"^\(?1?\)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})$"
    match = re.match(pattern, number)
    if not match:
        return False
    area_code = match.group(1)
    prefix = match.group(2)
    line_number = match.group(3)
    if area_code.startswith("0") or area_code.startswith("1"):
        return False
    if prefix.startswith("0"):
        return False
    if line_number.startswith("0"):
        return False
    return True

if __name__ == '__main__':
    print(is_valid_us_phone("(123) 456-7890"))
    print(is_valid_us_phone("123-456-7890"))
    print(is_valid_us_phone("1234567890"))
    print(is_valid_us_phone("023-456-7890"))
    print(is_valid_us_phone("123-056-7890"))