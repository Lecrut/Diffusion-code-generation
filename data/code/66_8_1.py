def kilometers_to_meters(kilometers):
    if kilometers < 0:
        raise ValueError("Input must be a non-negative number")
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