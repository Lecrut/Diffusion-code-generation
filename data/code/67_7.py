def liters_to_milliliters(liters: float) -> float:
    if not isinstance(liters, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    return liters * 1000

if __name__ == '__main__':
    sample_values = [1, 2.5, 0, -1.5]
    for val in sample_values:
        result = liters_to_milliliters(val)
        print(result)

    try:
        liters_to_milliliters("invalid")
    except TypeError as e:
        print(str(e))