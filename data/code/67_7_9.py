def convert_to_milliliters(value: float) -> int:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a numeric type, got {type(value).__name__}")
    return int(value * 1000)

if __name__ == '__main__':
    sample_liters = 2.5
    result = convert_to_milliliters(sample_liters)
    print(result)