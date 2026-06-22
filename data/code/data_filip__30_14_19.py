def decimal_to_binary(n: int) -> str:
    if n < 0:
        raise ValueError("n must be a positive decimal integer")
    if n == 0:
        return "0"
    return f"{n:b}"

if __name__ == '__main__':
    value = 10
    result = decimal_to_binary(value)
    print(result)