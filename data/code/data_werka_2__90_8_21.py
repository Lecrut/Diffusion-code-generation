def check_condition(*args):
    if not args:
        raise ValueError("At least one boolean argument is required")
    for arg in args:
        if not isinstance(arg, bool):
            raise TypeError(f"Expected bool, got {type(arg).__name__}")
    return any(args)

if __name__ == '__main__':
    sample_inputs = (False, False, True, False)
    result = check_condition(*sample_inputs)
    print(result)