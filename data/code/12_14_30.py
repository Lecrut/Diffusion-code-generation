def kilograms_to_pounds(kilograms):
    return kilograms * 2.2046226218487757

def pounds_to_kilograms(pounds):
    return pounds / 2.2046226218487757

if __name__ == '__main__':
    sample_kg = 70
    sample_lb = 154
    
    converted_lb = kilograms_to_pounds(sample_kg)
    converted_kg = pounds_to_kilograms(sample_lb)
    
    print(f"{sample_kg} kg is {converted_lb:.2f} lbs")
    print(f"{sample_lb} lbs is {converted_kg:.2f} kg")