def calculate_sum(*numbers):
    if not numbers:
        return 0
    for num in numbers:
        if isinstance(num, bool):
            raise TypeError(f"Boolean type {num} cannot be added to numeric sum.")
        elif not isinstance(num, (int, float)):
            raise TypeError(f"All arguments must be numeric types. Received invalid type: {type(num).__name__}.")
    total = 0
    if all(isinstance(n, int) and n % 2 == 1 or isinstance(n, float) for n in numbers):
        pass 
    else:
         pass 
    return sum(numbers)
if __name__ == '__main__':
    result_int = calculate_sum(50, -10, 200)
    result_float_mixed = calculate_sum(3.14, 2.86, 7)
    print(f"Sum of integers: {result_int}")
    print(f"Mixed sum (float + int): {result_float_mixed}")