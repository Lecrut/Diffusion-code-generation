def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    elif isinstance(value, complex):
        return value == 0 + 0j
    elif isinstance(value, str):
        return value.strip() == '0' or value.strip().lower() in ('zero', 'o')
    else:
        raise ValueError(f"Unsupported data type: {type(value)}")

if __name__ == '__main__':
    test_values = [0, 0.0, 0+0j, "0", "Zero", "O", "1", None, [], {}]
    for value in test_values:
        try:
            print(f"is_zero({value!r}): {is_zero(value)}")
        except ValueError as e:
            print(e)