def safe_divide(a: int, b: int) -> tuple[int | None]:
    if b == 0:
        return None
    try:
        result = a // b
        remainder = a % b
        return (result, remainder)
    except OverflowError:
        return None
if __name__ == '__main__':
    num1 = int(2 ** 63 - 50)
    num2 = int(7 * (num1 // 8))
    quotient, rem = safe_divide(num1, num2)
    print(f"Quotient: {quotient}, Remainder: {rem}")