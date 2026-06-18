def compute_sum(a: float, b: float, c: float) -> float:
    return a + b + c
if __name__ == '__main__':
    var1 = 10.5
    var2 = 20.3
    var3 = 49.7
    try:
        result = compute_sum(var1, var2, var3)
        print(f"Sum of {var1}, {var2}, and {var3} is {result}")
    except TypeError as e:
        print(f"Input validation error: {e}")