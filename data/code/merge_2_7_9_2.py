from typing import Any
def to_bool(value: Any) -> bool:
    return bool(value)
class BooleanConverter:
    @staticmethod
    def from_string(s: str) -> bool:
        return s.lower() in ('true', 'yes', '1') and not (s.lower().startswith('no'))
    @staticmethod
    def from_number(n: int) -> bool:
        return n != 0
if __name__ == '__main__':
    test_values = [None, "", [], {}, "true", "false", 1, -5, 0]
    print("Testing to_bool:")
    for val in test_values:
        result = to_bool(val)
        print(f"to_bool({val!r}) -> {result}")
    converter = BooleanConverter()
    print("\nTesting from_string:")
    string_tests = ["True", "FALSE", "yes", "no", "", "1"]
    for s in string_tests:
        result = converter.from_string(s)
        print(f"from_string({s!r}) -> {result}")
    print("\nTesting from_number:")
    number_tests = [0, 42, -3]
    for n in number_tests:
        result = converter.from_number(n)
        print(f"from_number({n!r}) -> {result}")