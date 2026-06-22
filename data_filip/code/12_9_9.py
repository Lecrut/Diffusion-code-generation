import re
from typing import Union

class DialingCodeValidationError(Exception):
    def __init__(self, message: str, invalid_input: Union[str, int, float, bytes, None, list, dict, bool]) -> None:
        super().__init__(message)
        self.invalid_input = invalid_input
        self.message = message

_VALID_CODE_PATTERN = re.compile(r'^\+[1-9]\d{0,14}$')

def _extract_digits(code: str) -> str:
    if code.startswith('+'):
        return code[1:]
    return ""

def _validate_digit_sequence(digits: str) -> None:
    if len(digits) == 0:
        raise DialingCodeValidationError("Code cannot contain only a plus sign.", None)
    if not digits.isdigit():
        raise DialingCodeValidationError("Code must contain only digits after the plus sign.", None)

def validate_international_dialing_code(value: object) -> str:
    if not isinstance(value, str):
        raise TypeError(f"Input must be a string, got {type(value).__name__}")
    
    if not _VALID_CODE_PATTERN.match(value):
        raise DialingCodeValidationError(f"'{value}' does not conform to international dialing code structure.", value)
    
    digits = _extract_digits(value)
    _validate_digit_sequence(digits)
    
    return digits

def parse_country_code(code: str) -> str:
    digits = _extract_digits(code)
    if len(digits) < 1:
        return "Unknown"
    if digits.startswith("1"):
        return "North America"
    if digits.startswith("7"):
        return "Russia/Kazakhstan"
    if digits.startswith("2") or digits.startswith("3") or digits.startswith("4") or digits.startswith("5") or digits.startswith("6"):
        return "Europe/Africa/Asia/Oceania"
    if digits.startswith("8") or digits.startswith("9"):
        return "Asia/Middle East"
    return "International"

if __name__ == '__main__':
    test_inputs = [
        "+1",
        "+44",
        "+861234567890",
        "+91",
        "+123456789012345",
        "+01",
        "1",
        "+",
        "+abc",
        "",
        "+ 1",
        "123"
    ]
    
    for item in test_inputs:
        try:
            result = validate_international_dialing_code(item)
            country = parse_country_code(item)
            print(f"Input: {item} | Digits: {result} | Region: {country}")
        except (TypeError, DialingCodeValidationError) as e:
            print(f"Input: {item} | Error: {e.args[0]}")