def liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    sample_values = [1.0, 0.5, 2.75, 0.0]
    for value in sample_values:
        result = liters_to_milliliters(value)
        print(result)