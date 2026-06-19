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
    sample_feet = 30
    sample_kilograms = 50
    sample_pounds = 110

    converted_feet = meters_to_feet(sample_meters)
    converted_meters = feet_to_meters(sample_feet)
    converted_pounds = kilograms_to_pounds(sample_kilograms)
    converted_kilograms = pounds_to_kilograms(sample_pounds)

    print(f"{sample_meters} meters is {converted_feet} feet")
    print(f"{sample_feet} feet is {converted_meters} meters")
    print(f"{sample_kilograms} kilograms is {converted_pounds} pounds")
    print(f"{sample_pounds} pounds is {converted_kilograms} kilograms")