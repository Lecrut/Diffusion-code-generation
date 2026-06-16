from typing import Any, TypeVar
T = TypeVar('T')
class SequenceReverser:
    @staticmethod
    def reverse_list(seq: list) -> list:
        if not isinstance(seq, list):
            raise TypeError("Input must be a list.")
        return seq[::-1]
    @staticmethod
    def reverse_tuple(seq: tuple) -> tuple:
        if not isinstance(seq, tuple):
            raise TypeError("Input must be a tuple.")
        return seq[::-1]
    @staticmethod
    def reverse_set(seq: set) -> list:
        if not isinstance(seq, set):
            raise TypeError("Input must be a set.")
        return list(seq)[::-1]
    @staticmethod
    def reverse_string(s: str) -> str:
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        return s[::-1]
if __name__ == '__main__':
    test_cases = [
        ("List", ["apple", "banana", "cherry"]),
        ("Tuple", (1, 2, 3)),
        ("Set", {5, 4, 6}),
        ("String", "Hello"),
        ("Invalid Type for List", {"not": "a list"}),
    ]
    results = []
    for name, value in test_cases:
        try:
            if isinstance(value, (list, tuple)):
                reversed_val = SequenceReverser.reverse_list(value) if not isinstance(value, tuple) else SequenceReverser.reverse_tuple(value)
                result_msg = f"{name}: {reversed_val}"
            elif isinstance(value, set):
                reversed_val = SequenceReverser.reverse_set(value)
                result_msg = f"{name} (Set converted to list): {reversed_val}"
            elif isinstance(value, str):
                reversed_val = SequenceReverser.reverse_string(value)
                result_msg = f"{name}: '{reversed_val}'"
            else:
                raise ValueError("Unsupported type for this test case.")
        except Exception as e:
            result_msg = f"{name} Error: {str(e)}"
        results.append(result_msg)
    print("\n".join(results))