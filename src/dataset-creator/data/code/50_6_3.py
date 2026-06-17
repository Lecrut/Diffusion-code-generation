def conditional_sum(a: float | int, b: float | int, c: float | int) -> float | None:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        return a + b + c
    return None
if __name__ == '__main__':
    x = 10.5
    y = "hello"
    z = 20
    result = conditional_sum(x, y, z) if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)) else None
    total: float | int | None = ((x + y + z) if all(isinstance(v, (int, float)) for v in [x, y, z]) else 0.0)
    print(total)