import re

def is_valid_e164(phone: str) -> bool:
    return bool(re.fullmatch(r'\+[1-9]\d{1,14}', phone))

if __name__ == '__main__':
    print(is_valid_e164("+14155552671"))
    print(is_valid_e164("+442071838750"))
    print(is_valid_e164("14155552671"))
    print(is_valid_e164("+000"))