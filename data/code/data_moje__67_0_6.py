def convert_to_milliliters(liters: list[float]) -> list[float]:
    return [l * 1000 for l in liters]

if __name__ == '__main__':
    liters_list = [1.5, 2.0, 0.75]
    result = convert_to_milliliters(liters_list)
    print(result)