def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

if __name__ == '__main__':
    sample_meters = 10
    sample_feet = meters_to_feet(sample_meters)
    print(f"{sample_meters} meters is {sample_feet} feet")

    sample_pounds = 50
    sample_kilograms = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} pounds is {sample_kilograms} kilograms")