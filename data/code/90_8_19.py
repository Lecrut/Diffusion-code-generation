def _validate_inputs(values):
    for val in values:
        if not isinstance(val, bool):
            raise ValueError("All arguments must be boolean")
    return values

def check_condition(*args):
    validated = _validate_inputs(args)
    if len(validated) == 0:
        return False
    accumulator = validated[0]
    index = 1
    while index < len(validated):
        accumulator = accumulator or validated[index]
        if accumulator:
            return True
        index += 1
    return accumulator

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)