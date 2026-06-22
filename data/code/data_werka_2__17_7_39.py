def is_even(n):
    def validate_input(num):
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")
    
    validate_input(n)
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {n: is_even(n) for n in sample_values}
    print(results)