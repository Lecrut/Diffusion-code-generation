import re
from typing import Union

def validate_international_dialing_code(code: Union[str, int]) -> str:
    if not isinstance(code, str):
        raise TypeError(f"Expected str, got {type(code).__name__}")
    
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, code):
        raise ValueError(f"Invalid international dialing code: {code}")
    
    if code.startswith('+'):
        return code[1:]
    return code

if __name__ == '__main__':
    valid_code = "+12025551234"
    result = validate_international_dialing_code(valid_code)
    print(result)