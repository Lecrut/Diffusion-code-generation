def check_or_condition(a: bool, b: bool) -> bool:
    def validate_bool(val: bool) -> bool:
        if not isinstance(val, bool):
            raise ValueError("Input must be a boolean type")
        return bool(val)
    
    valid_a = validate_bool(a)
    valid_b = validate_bool(b)
    
    return valid_a | valid_b

if __name__ == '__main__':
    result = check_or_condition(False, True)
    print(result)