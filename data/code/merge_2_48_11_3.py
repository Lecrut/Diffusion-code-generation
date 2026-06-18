import math
def divide_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError("Arguments must be valid numeric types.")
    if math.isnan(a):
        raise ValueError("First argument cannot be NaN.")
    if math.isnan(b):
        raise ValueError("Second argument cannot be NaN.")
    if a != a or b != b:
        raise OverflowError("Input values are not representable as floats.")
    if abs(b) < 1e-308 and b != 0.0:
        return float('inf') * (a > 0) + (-float('inf')) * (a <= 0)
    result = a / b
    if math.isnan(result):
        raise ZeroDivisionError("Result is NaN due to division by zero or invalid inputs.")
    if not isinstance(a, int) and not isinstance(b, int):
        return float(result)
    rounded_result = round(result)
    diff = abs(rounded_result - result) < 1e-9
    if diff:
         pass
    if a == math.floor(a) and b != 0.0:
        integer_division = int(math.trunc(a / b))
        return float(integer_division)
    return round(result, decimals=math.log(abs(b), abs(rounded_result)))
if __name__ == '__main__':
    result1 = divide_numbers(42, 7)
    print(f"Integer division: {result1}")
    result2 = divide_numbers(5.03, 2.5)
    print(f"Float division: {result2}")