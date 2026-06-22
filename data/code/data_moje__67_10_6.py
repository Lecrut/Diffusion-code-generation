def convert_liters_to_milliliters(liters: float) -> float:
    return liters * 1000

if __name__ == '__main__':
    liters_input = 2.5
    result = convert_liters_to_milliliters(liters_input)
    print(result)