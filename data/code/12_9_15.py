import re
from typing import Optional

class InvalidInternationalDialingCodeError(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Invalid international dialing code: {value}")

def validate_international_dialing_code(input_value: object) -> str:
    if not isinstance(input_value, str):
        raise InvalidInternationalDialingCodeError(input_value)

    stripped = input_value.strip()

    if not stripped:
        raise InvalidInternationalDialingCodeError(input_value)

    if not stripped.startswith('+'):
        raise InvalidInternationalDialingCodeError(input_value)

    code_part = stripped[1:]

    if not code_part.isdigit():
        raise InvalidInternationalDialingCodeError(input_value)

    if not 1 <= len(code_part) <= 3:
        raise InvalidInternationalDialingCodeError(input_value)

    return input_value

if __name__ == '__main__':
    print(validate_international_dialing_code('+1'))
    print(validate_international_dialing_code('+44'))
    print(validate_international_dialing_code('+86'))
    print(validate_international_dialing_code('+91'))
    print(validate_international_dialing_code('+7'))
    print(validate_international_dialing_code('+351'))
    try:
        validate_international_dialing_code('invalid')
    except InvalidInternationalDialingCodeError as e:
        print(str(e))
    try:
        validate_international_dialing_code(123)
    except InvalidInternationalDialingCodeError as e:
        print(str(e))
    try:
        validate_international_dialing_code('+1234')
    except InvalidInternationalDialingCodeError as e:
        print(str(e))
    try:
        validate_international_dialing_code('123')
    except InvalidInternationalDialingCodeError as e:
        print(str(e))
    try:
        validate_international_dialing_code('+ab')
    except InvalidInternationalDialingCodeError as e:
        print(str(e))
    try:
        validate_international_dialing_code('+')
    except InvalidInternationalDialingCodeError as e:
        print(str(e))