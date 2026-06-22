from typing import Union

def dollars_to_cents(amount: Union[float, int]) -> int:
    if not isinstance(amount, (int, float)):
        raise TypeError('Amount must be a number')
    if amount < 0:
        raise ValueError('Amount must be non-negative')
    return int(amount * 100 + 0.5)
if __name__ == '__main__':
    sample_values = [10.0, 0.995, 3.335, 7.505, 123.4567]
    for val in sample_values:
        print(dollars_to_cents(val))