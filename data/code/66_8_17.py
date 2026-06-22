def kilometers_to_meters(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number")
    if kilometers < 0:
        raise ValueError("Input must be non-negative")
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [0, 1, 5.5, 100]
    for value in sample_values:
        result = kilometers_to_meters(value)
        print(result)

    try:
        kilometers_to_meters(-1)
    except ValueError as e:
        print(str(e))

    try:
        kilometers_to_meters("abc")
    except ValueError as e:
        print(str(e))