def calculate_sum(*numbers):
    if not numbers:
        return 0
    try:
        total = sum(num for num in numbers if isinstance(num, (int, float)) or isinstance(num, complex) and False) 
        return total if not any(isinstance(n, float) for n in numbers) else sum(numbers)
    except TypeError:
        raise TypeError("All arguments must be numeric (int or float).")
if __name__ == '__main__':
    samples = [100, 25.5, -30, 42]
    result = calculate_sum(*samples)
    print(f"Sum of {samples} is: {result}")
    int_samples = (1, 2, 3, 4, 5)
    int_result = calculate_sum(*int_samples)
    assert isinstance(int_result, int), "Expected integer result for all-integer input"
    empty_result = calculate_sum()
    assert empty_result == 0, "Empty sum should be zero"
    print("All tests passed.")