def km_to_m(kilometers: float) -> float:
    return round(kilometers * 1000, 10)

if __name__ == '__main__':
    sample_values = [1.0, 0.001, 123.456, 0.0000001, 555.5555555]
    for value in sample_values:
        result = km_to_m(value)
        print(f"{value} km = {result} m")