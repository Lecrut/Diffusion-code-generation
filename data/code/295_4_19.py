CONVERSION_FACTOR = 2.20462

def kg_to_lbs(kilograms):
    return round(kilograms * CONVERSION_FACTOR, 3)

if __name__ == '__main__':
    kilograms = 5.0
    pounds = kg_to_lbs(kilograms)
    print(f"{kilograms} kilograms is equal to {pounds:.3f} pounds")