def is_strictly_less_than_zero(value: float) -> bool:
    return value < 0
if __name__ == '__main__':
    print(f"is_strictly_less_than_zero(-5.0): {is_strictly_less_than_zero(-5.0)}")
    print(f"is_strictly_less_than_zero(0.0): {is_strictly_less_than_zero(0.0)}")
    print(f"is_strictly_less_than_zero(1.5): {is_strictly_less_than_zero(1.5)}")
    print(f"is_strictly_less_than_zero(-0.001): {is_strictly_less_than_zero(-0.001)}")