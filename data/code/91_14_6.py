from typing import Union

def flip_bool_value(value: Union[bool, int]) -> bool:
    if not isinstance(value, bool) and not isinstance(value, int):
        raise ValueError("Input must be a boolean or integer")
    if isinstance(value, int):
        if value not in (0, 1):
            raise ValueError("Integer input must be 0 or 1")
        return bool(not value)
    return not value

if __name__ == '__main__':
    result_true = flip_bool_value(True)
    result_false = flip_bool_value(False)
    result_zero = flip_bool_value(0)
    result_one = flip_bool_value(1)
    print(result_true)
    print(result_false)
    print(result_zero)
    print(result_one)