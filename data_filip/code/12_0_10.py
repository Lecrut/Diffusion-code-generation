import re

def is_e164(phone_number: str) -> bool:
    pattern = r'^\+[1-9]\d{10,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_number = "+14155552671"
    result = is_e164(sample_number)
    print(result)