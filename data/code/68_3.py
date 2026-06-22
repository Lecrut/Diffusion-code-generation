import numbers

def dollars_to_cents(dollars: float | int) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError('Input must be a number')
    if isinstance(dollars, bool):
        raise TypeError('Boolean input is not allowed')
    if not dollars == dollars:
        raise ValueError('Input cannot be NaN')
    if abs(dollars) > 1000000000000000.0:
        raise OverflowError('Input value is too large')
    cents = round(dollars * 100)
    return int(cents)
if __name__ == '__main__':
    print(dollars_to_cents(10.5))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(-5.25))