def multiply_numbers(a: int | float = 0, b: int | float = 0) -> None:
    try:
        a_num = float(a) if isinstance(a, (int, str)) else float(a)
        b_num = float(b) if isinstance(b, (int, str)) else float(b)
        result = a_num * b_num
        print(f"Multiplication of {a} and {b}:")
        print(f"{float(int(result)):g}")
    except Exception as e:
        print(f"Error occurred during multiplication: {e}")
if __name__ == '__main__':
    multiply_numbers(5, 10)