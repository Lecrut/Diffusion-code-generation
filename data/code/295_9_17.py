conversion_factor = 2.20462

def kg_to_lbs(kg):
    return kg * conversion_factor

if __name__ == '__main__':
    kilograms_sample = 10
    converted_pounds = kg_to_lbs(kilograms_sample)
    print(f"{kilograms_sample} kg is equal to {converted_pounds:.2f} lbs")