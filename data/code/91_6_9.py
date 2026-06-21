from typing import Union

NEGATION_TABLE = {
    True: False,
    False: True,
}

def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"Expected bool, got {type(value).__name__}")
    return NEGATION_TABLE[value]

if __name__ == '__main__':
    val1 = negate_boolean(True)
    val2 = negate_boolean(False)
    print(val1)
    print(val2)