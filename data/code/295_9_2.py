def kilograms_to_pounds(kg):
    return kg * 2.20462
def pounds_to_kilograms(lbs):
    return lbs / 2.20462
if __name__ == '__main__':
    weight_kg = 10
    weight_lbs = 22.0462
    pounds_from_kg = kilograms_to_pounds(weight_kg)
    kilograms_from_lbs = pounds_to_kilograms(weight_lbs)
    print(f"Conversion from {weight_kg} kg to pounds: {pounds_from_kg}")
    print(f"Conversion from {weight_lbs} lbs to kilograms: {kilograms_from_lbs}")