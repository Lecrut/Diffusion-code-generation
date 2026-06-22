def liters_to_milliliters(liters: list[float]) -> list[float]:
    return [liter * 1000 for liter in liters]

if __name__ == '__main__':
    sample_liters = [1.0, 2.5, 0.75, 3.33]
    result = liters_to_milliliters(sample_liters)
    print(result)