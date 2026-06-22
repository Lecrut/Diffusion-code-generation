CONVERSION_FACTOR_KG_TO_LBS = 2.20462

def pounds_to_kilograms(pounds):
    return pounds / CONVERSION_FACTOR_KG_TO_LBS

if __name__ == '__main__':
    sample_pounds = 150
    result_kg = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is equal to {result_kg:.2f} kg")