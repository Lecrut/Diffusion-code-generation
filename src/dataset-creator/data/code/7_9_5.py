def to_bool(value: bool | int | str) -> bool:
    try:
        return bool(value)
    except Exception as e:                
        raise TypeError(f"Cannot convert {type(value).__name__} to bool") from e
def is_truthy(value: object) -> bool:
    try:
        return bool(value)
    except Exception as e:                
        raise TypeError(f"Cannot evaluate {type(value).__name__} for truthiness") from e
def to_boolean(value: object | None = None) -> bool:
    return bool(value)
if __name__ == '__main__':
    test_cases = [True, 1, "yes", "", -5, [], {}, set(), object()]
    print("Testing to_bool:")
    for val in test_cases:
        try:
            result = to_bool(val)
            print(f"to_bool({val!r}) -> {result}")
        except TypeError as e:
            print(f"to_bool({val!r}) raised TypeError")
    print("\nTesting is_truthy:")
    for val in test_cases:
        try:
            result = is_truthy(val)
            print(f"is_truthy({val!r}) -> {result}")
        except TypeError as e:
            print(f"is_truthy({val!r}) raised TypeError")
    print("\nTesting to_boolean:")
    for val in test_cases + [None, False]:
        try:
            result = to_boolean(val)
            print(f"to_boolean({val!r}) -> {result}")
        except TypeError as e:
            print(f"to_boolean({val!r}) raised TypeError")