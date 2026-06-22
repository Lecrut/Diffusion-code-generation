conversion_factor = 2.20462

def pounds_to_kg(pounds):
    return pounds / conversion_factor

if __name__ == '__main__':
    sample_pounds = 22.0462
    converted_kg = pounds_to_kg(sample_pounds)
    print(f"{sample_pounds:.2f} lbs is equal to {converted_kg:.2f} kg")