conversion_factor = {"kg_to_lbs": 2.20462, "lbs_to_kg": 1 / 2.20462}

def get_conversion_factor(direction):
    return conversion_factor.get(direction, None)

if __name__ == '__main__':
    pounds_conversion = get_conversion_factor("kg_to_lbs")
    kilograms_conversion = get_conversion_factor("lbs_to_kg")
    
    print(f"Pounds to Kilograms conversion factor: {pounds_conversion:.2f}")
    print(f"Kilograms to Pounds conversion factor: {kilograms_conversion:.2f}")