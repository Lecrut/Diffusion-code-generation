def validate_flags(a: bool, b: bool) -> bool:
    if not (a and b):
        raise ValueError('At least one flag is false')
    return True

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    try:
        result = validate_flags(sample_a, sample_b)
        print(result)
    except ValueError as e:
        print(e)