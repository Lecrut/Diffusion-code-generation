def kg_to_lbs(kilograms):
    return kilograms * 2.20462

if __name__ == '__main__':
    weight_kg = 50.0
    weight_lbs = kg_to_lbs(weight_kg)
    print(f"{weight_kg} kg is equal to {weight_lbs:.2f} lbs")