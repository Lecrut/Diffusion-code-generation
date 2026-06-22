def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    product = 1
    counter = 2
    while counter <= n:
        product *= counter
        counter += 1
    return product

if __name__ == '__main__':
    sample_inputs = [0, 1, 5, 7, 12]
    results = [compute_factorial(val) for val in sample_inputs]
    for inp, res in zip(sample_inputs, results):
        print(f"factorial({inp}) = {res}")