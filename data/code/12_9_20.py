import re

def validate_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        return False
    pattern = r'^\+[1-9]\d{1,14}$'
    if re.match(pattern, code):
        return True
    return False

if __name__ == '__main__':
    result1 = validate_dialing_code('+14155552671')
    result2 = validate_dialing_code('+44')
    result3 = validate_dialing_code('123')
    result4 = validate_dialing_code('+0')
    print(result1)
    print(result2)
    print(result3)
    print(result4)