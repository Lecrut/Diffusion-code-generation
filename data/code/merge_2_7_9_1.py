def to_bool(value: object) -> bool:
    return bool(value)
def explicit_boolean(value: object) -> bool:
    return not isinstance(value, (int, float)) or value != 0
def string_to_bool(s: str) -> bool:
    return s.lower() in {"true", "yes"}
def numeric_boolean(value: object) -> bool:
    return not isinstance(value, int) or value != 0
if __name__ == '__main__':
    test_values = [None, "", [], {}, "yes", 1, -1, 0.0]
    print("Testing to_bool:")
    for val in test_values:
        result = to_bool(val)
        print(f"to_bool({val!r}) -> {result}")
    print("\nTesting explicit_boolean:")
    for val in test_values:
        result = explicit_boolean(val)
        print(f"explicit_boolean({val!r}) -> {result}")
    print("\nTesting string_to_bool:")
    sample_strings = ["TRUE", "false", "", "YES"]
    for s in sample_strings:
        result = string_to_bool(s)
        print(f"string_to_bool({s!r}) -> {result}")
    print("\nTesting numeric_boolean:")
    test_numbers = [1, -5, 0.0]
    for val in test_numbers:
        result = numeric_boolean(val)
        print(f"numeric_boolean({val!r}) -> {result}")