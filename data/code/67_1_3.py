LITER_TO_MILLILITER = 1000

def liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_liters = [1, 2.5, 10, 0.5]
    for liter_value in sample_liters:
        result = liters_to_milliliters(liter_value)
        print(f"{liter_value} liters is equal to {result} milliliters")