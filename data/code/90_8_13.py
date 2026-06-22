def check_condition(*args):
    if not args:
        raise ValueError("At least one boolean argument is required")
    
    def validate(val):
        if not isinstance(val, bool):
            raise TypeError(f"Expected boolean, got {type(val).__name__}")
        return val
    
    validated_args = tuple(validate(a) for a in args)
    
    accumulator = False
    for val in validated_args:
        accumulator = accumulator or val
        if accumulator:
            break
    return accumulator

if __name__ == '__main__':
    sample_values = (False, False, True, False)
    result = check_condition(*sample_values)
    print(result)