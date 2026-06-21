import re

def normalize_phone(phone_str: str) -> bool:
    digits_only = re.sub(r'\D', '', phone_str)
    return len(digits_only) == 11

if __name__ == '__main__':
    result = normalize_phone("123-456-78901")
    print(result)
    result2 = normalize_phone("123-456-7890")
    print(result2)