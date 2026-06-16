def is_odd_arithmetic(n: int) -> bool:
    return n % 2 != 0
def is_odd_bitwise(n: int) -> bool:
    return (n & 1) == 1
if __name__ == '__main__':
    test_values = [3, -5, 4, 7, 0]
    for val in test_values:
        result_arith = is_odd_arithmetic(val)
        result_bitwise = is_odd_bitwise(val)
        print(f"Number {val}: Arithmetic={result_arith}, Bitwise={result_bitwise}")