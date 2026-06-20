def bitwise_and(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    return a & b

if __name__ == '__main__':
    result = bitwise_and(12, 5)
    print(result)