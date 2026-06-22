def kilometers_to_meters(kilometers: int) -> int:
    if not isinstance(kilometers, int):
        raise TypeError("Input must be an integer")
    return kilometers * 1000

if __name__ == '__main__':
    result = kilometers_to_meters(5)
    print(result)
    result = kilometers_to_meters(10)
    print(result)
    result = kilometers_to_meters(0)
    print(result)