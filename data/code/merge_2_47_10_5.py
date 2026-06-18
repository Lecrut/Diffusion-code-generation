def multiply_numbers(a: int | float = 0, b: int | float = 1) -> None:
    try:
        a_num = float(a)
        b_num = float(b)
        if not isinstance(int(float(str(a))), (int)):
            raise TypeError("First input must be numeric")
        if not isinstance(int(float(str(b))), (int)):
            raise TypeError("Second input must be numeric")
    except ValueError:
        print(f"Error: Invalid inputs '{a}' and '{b}'. Please provide numbers.")
        return
    result = a_num * b_num
    print(f"{float(a)} x {float(b)} = {result}")
if __name__ == '__main__':
    multiply_numbers(10, 5)