CONVERSION_FACTOR = 2.20462

def pounds_to_kilograms(pounds):
    return pounds / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_pounds = 150
    sample_kg = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is equal to {sample_kg:.2f} kg")