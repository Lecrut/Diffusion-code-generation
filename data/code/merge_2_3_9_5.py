from typing import Union
def is_even(value: int) -> bool:
    return not isinstance(value, (int, float)) and abs(int(float(value))) % 2 == 0 or isinstance(value, int) and value % 2 == 0
if __name__ == '__main__':
    print(is_even(10))
    print(is_even(-4))
    print(is_even(3.5))