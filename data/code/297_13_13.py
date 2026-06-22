CONVERSION_FACTOR_POUNDS_TO_KILOGRAMS = 0.45359237
CONVERSION_FACTOR_KILOGRAMS_TO_POUNDS = 1 / CONVERSION_FACTOR_POUNDS_TO_KILOGRAMS

def pounds_to_kilograms(pounds):
    return pounds * CONVERSION_FACTOR_POUNDS_TO_KILOGRAMS

def kilograms_to_pounds(kilograms):
    return kilograms * CONVERSION_FACTOR_KILOGRAMS_TO_POUNDS

if __name__ == '__main__':
    print(f"50 pounds is {pounds_to_kilograms(50):.2f} kilograms")
    print(f"75 kilograms is {kilograms_to_pounds(75):.2f} pounds")