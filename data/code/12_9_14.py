class InvalidDialingCodeError(Exception):
    def __init__(self, code: str) -> None:
        super().__init__(f"Invalid international dialing code: {code}")
        self.code = code

class DialingCodeValidator:
    MIN_DIGITS = 1
    MAX_DIGITS = 14
    MAX_LENGTH = 15

    def validate(self, code: str) -> bool:
        if not isinstance(code, str):
            raise TypeError("Input must be a string")
        
        if not code.startswith('+'):
            raise InvalidDialingCodeError(code)
        
        numeric_part = code[1:]
        
        if not numeric_part:
            raise InvalidDialingCodeError(code)
        
        if not numeric_part.isdigit():
            raise InvalidDialingCodeError(code)
        
        first_digit = int(numeric_part[0])
        if first_digit == 0:
            raise InvalidDialingCodeError(code)
        
        if len(numeric_part) < self.MIN_DIGITS or len(numeric_part) > self.MAX_DIGITS:
            raise InvalidDialingCodeError(code)
        
        return True

def validate_international_dialing_code(code: str) -> bool:
    validator = DialingCodeValidator()
    return validator.validate(code)

if __name__ == '__main__':
    samples = ["+1", "+44", "+86", "+7", "+91", "+123456789012", "+01", "+abc", "123", "+", ""]
    for sample in samples:
        try:
            result = validate_international_dialing_code(sample)
            print(f"{sample}: {result}")
        except (TypeError, InvalidDialingCodeError) as e:
            print(f"{sample}: Error - {e}")