def _validate_bool(value):
    if not isinstance(value, bool):
        raise ValueError("All arguments must be boolean values")
    return value

def check_condition(*args):
    validated_args = tuple(_validate_bool(arg) for arg in args)
    current_result = False
    for val in validated_args:
        current_result = current_result or val
        if current_result:
            break
    return current_result

if __name__ == '__main__':
    sample_values = (True, False, False)
    output = check_condition(*sample_values)
    print(output)