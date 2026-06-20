def validate_boolean_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def get_opposite(boolean: bool) -> bool:
    return not boolean

if __name__ == '__main__':
    sample1 = True
    try:
        validate_boolean_input(sample1)
        result1 = get_opposite(sample1)
        print(f"Input: {sample1}, Output: {result1}")
        
        sample2 = False
        validate_boolean_input(sample2)
        result2 = get_opposite(sample2)
        print(f"Input: {sample2}, Output: {result2}")
    except ValueError as e:
        print(f"Error: {e}")