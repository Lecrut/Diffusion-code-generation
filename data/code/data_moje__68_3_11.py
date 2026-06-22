from typing import Union

def dollars_to_cents(dollars: Union[int, float]) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    if isinstance(dollars, float):
        if dollars != dollars or dollars == float('inf') or dollars == float('-inf'):
            raise ValueError("Input must be a finite number")
    if dollars < 0:
        raise ValueError("Input must be non-negative")
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1))
    print(dollars_to_cents(1.50))
    print(dollars_to_cents(100))