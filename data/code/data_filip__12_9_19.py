import re
from typing import Union

class InternationalDialingCode:
    def __init__(self, code: str) -> None:
        if not isinstance(code, str):
            raise TypeError("Input must be a string")
        if not re.match(r'^\+?[1-9]\d{1,14}$', code):
            raise ValueError("Invalid international dialing code format")
        self.code = code

def validate_dialing_code(input_value: str) -> str:
    if not isinstance(input_value, str):
        raise TypeError("Input argument must be a string")
    code_obj = InternationalDialingCode(input_value)
    return code_obj.code

if __name__ == '__main__':
    sample_valid = "+1234567890"
    sample_invalid_format = "12abc"
    sample_invalid_type = 12345

    print(validate_dialing_code(sample_valid))

    try:
        validate_dialing_code(sample_invalid_format)
    except ValueError as e:
        print(str(e))

    try:
        validate_dialing_code(sample_invalid_type)
    except TypeError as e:
        print(str(e))