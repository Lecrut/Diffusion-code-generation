CONVERSION_FACTOR_TON_TO_KG = 1000

def tons_to_kg(tons):
    kilograms = tons * CONVERSION_FACTOR_TON_TO_KG
    return int(kilograms)

if __name__ == '__main__':
    sample_tons = 5
    result_kg = tons_to_kg(sample_tons)
    print(f"{sample_tons} ton is {result_kg} kg")