def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    is_false = value == False
    return is_false

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    result_true = negate_boolean(sample_true)
    result_false = negate_boolean(sample_false)
    print(result_true)
    print(result_false)