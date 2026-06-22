GALLON_TO_LITER = 3.78541

def convert_gallons_to_liters(gallons):
    return gallons * GALLON_TO_LITER
if __name__ == '__main__':
    print(convert_gallons_to_liters(1))
    print(convert_gallons_to_liters(10))