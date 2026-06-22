CONVERSION_FACTOR_KG_TO_LBS = 2.20462

def kg_to_lbs(kg):
    return kg * CONVERSION_FACTOR_KG_TO_LBS

if __name__ == '__main__':
    kilograms = 10
    converted_pounds = kg_to_lbs(kilograms)
    print(f"{kilograms} kg is equal to {converted_pounds:.2f} lbs")