def kilometers_to_meters(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number")
    if kilometers < 0:
        raise ValueError("Input must be non-negative")
    return kilometers * 1000

if __name__ == '__main__':
    result = kilometers_to_meters(5)
    print(result)
    result2 = kilometers_to_meters(0)
    print(result2)
    try:
        kilometers_to_meters(-1)
    except ValueError as e:
        print(str(e))