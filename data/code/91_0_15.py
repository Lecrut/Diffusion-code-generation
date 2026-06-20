def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    sample_value = True
    try:
        result = negate_boolean(sample_value)
        print(f"Negation of {sample_value}: {result}")
    except ValueError as e:
        print(e)