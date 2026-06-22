def convert_liters_to_milliliters(liter_list):
    return list(map(lambda x: x * 1000, liter_list))

if __name__ == '__main__':
    liter_values = [1, 2.5, 10, 0.5]
    result = convert_liters_to_milliliters(liter_values)
    for liter, milliliter in zip(liter_values, result):
        print(f"{liter} liters is {milliliter} milliliters")