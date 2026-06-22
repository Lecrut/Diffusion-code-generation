def _validate_boolean(*args):
    for arg in args:
        if not isinstance(arg, bool):
            raise ValueError("All arguments must be boolean values")
    return args

def check_condition(*args):
    validated_args = _validate_boolean(*args)
    if not validated_args:
        return False
    result = validated_args[0]
    for val in validated_args[1:]:
        if result:
            return True
        result = val
    return result

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)