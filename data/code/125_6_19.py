def perform_operations(a: int, b: int) -> None:
    result_add = a + b
    result_subtract = a - b
    print(f"Addition of {a} and {b}: {result_add}")
    print(f"Subtraction of {a} and {b}: {result_subtract}")

if __name__ == '__main__':
    perform_operations(15, 7)