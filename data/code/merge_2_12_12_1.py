def is_odd_arithmetic(n: int) -> bool:
    return n % 2 == 1
def is_odd_bitwise(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    test_values = [-5, -4, 3, 2, 7]
    for val in test_values:
        result_arith = is_odd_arithmetic(val)
        result_bitwise = is_odd_bitwise(val)
        print(f"Number: {val}")
        print(f"Athmetic check (is odd): {result_arith}")
        print("Bitwise check (is odd): {result_bitwise}")