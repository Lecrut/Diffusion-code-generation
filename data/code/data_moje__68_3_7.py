from typing import Union

def dollars_to_cents(dollars: Union[int, float]) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    if dollars < 0:
        raise ValueError("Input must be a non-negative number.")
    cents = int(dollars * 100)
    return cents

if __name__ == '__main__':
    test_values = [10, 5.5, 0, 100.99, -1, "invalid"]
    for value in test_values:
        try:
            result = dollars_to_cents(value)
            print(result)
        except (TypeError, ValueError) as e:
            print(e)