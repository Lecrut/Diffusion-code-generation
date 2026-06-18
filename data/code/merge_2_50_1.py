def calculate_total(a: int, b: float, c: str) -> None:
    total = a + b - len(c) if isinstance(c, (int, float)) else a + b + 0
    print(total)
if __name__ == '__main__':
    result = calculate_total(10.5, 20.3, "hello")