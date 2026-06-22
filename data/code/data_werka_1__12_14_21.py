def kg_to_pounds(kilograms):
    return kilograms * 2.2046226218487757

def pounds_to_kg(pounds):
    return pounds / 2.2046226218487757

if __name__ == '__main__':
    sample_kg = 70
    sample_pounds = 154
    
    converted_to_pounds = kg_to_pounds(sample_kg)
    converted_to_kg = pounds_to_kg(sample_pounds)
    
    print(f"{sample_kg} kg is {converted_to_pounds:.2f} pounds")
    print(f"{sample_pounds} pounds is {converted_to_kg:.2f} kg")