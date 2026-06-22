def kilometers_to_meters(kilometers: int) -> int:
    if not isinstance(kilometers, int):
        raise TypeError("Input must be an integer")
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [0, 1, 5, 100, -3]
    for km in sample_values:
        result = kilometers_to_meters(km)
        print(result)