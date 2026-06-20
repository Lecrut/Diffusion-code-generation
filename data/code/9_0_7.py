def convert_liters_to_ml(value):
    return value * 1000

def convert_ml_to_liters(value):
    return value / 1000

def convert_liters_to_cubic_meters(value):
    return value / 1000

def convert_cubic_meters_to_liters(value):
    return value * 1000

def convert_liters_to_gallons(value):
    return value * 0.264172

def convert_gallons_to_liters(value):
    return value / 0.264172

def convert_liters_to_cubic_inches(value):
    return value * 61.0237

def convert_cubic_inches_to_liters(value):
    return value / 61.0237

def run_conversion_tests():
    test_liters = 5.0
    print(f"{test_liters} liters to milliliters: {convert_liters_to_ml(test_liters)}")
    print(f"{test_liters} liters to cubic meters: {convert_liters_to_cubic_meters(test_liters)}")
    print(f"{test_liters} liters to gallons: {convert_liters_to_gallons(test_liters)}")
    print(f"{test_liters} liters to cubic inches: {convert_liters_to_cubic_inches(test_liters)}")
    
    test_ml = 1000.0
    print(f"{test_ml} milliliters to liters: {convert_ml_to_liters(test_ml)}")
    
    test_cubic_m = 2.0
    print(f"{test_cubic_m} cubic meters to liters: {convert_cubic_meters_to_liters(test_cubic_m)}")
    
    test_gallons = 10.0
    print(f"{test_gallons} gallons to liters: {convert_gallons_to_liters(test_gallons)}")
    
    test_cubic_inches = 30.0
    print(f"{test_cubic_inches} cubic inches to liters: {convert_cubic_inches_to_liters(test_cubic_inches)}")

if __name__ == '__main__':
    run_conversion_tests()