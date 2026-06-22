LITER_TO_MILLILITER_FACTOR = 1000

def convert_liter_to_milliliter(volume_in_liters: float) -> float:
    return volume_in_liters * LITER_TO_MILLILITER_FACTOR

if __name__ == '__main__':
    liter_values = [1.5, 2.0, 0.25, 10.0]
    for liter in liter_values:
        milliliter = convert_liter_to_milliliter(liter)
        print(milliliter)