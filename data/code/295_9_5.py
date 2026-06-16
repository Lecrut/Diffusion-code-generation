def kilograms_to_pounds(kg):
    return kg * 2.20462
def pounds_to_kilograms(lbs):
    return lbs / 2.20462
if __name__ == '__main__':
    weight_kg = 10
    weight_lbs = 22.0462
    pounds_from_kg = kilograms_to_pounds(weight_kg)
    kilograms_from_lbs = pounds_to_kilograms(weight_lbs)
    print(f"10 kilograms is equal to {pounds_from_kg:.2f} pounds")
    print(f"22.0462 pounds is equal to {kilograms_from_lbs:.2f} kilograms")