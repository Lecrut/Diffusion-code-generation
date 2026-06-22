GALLONS_TO_LITERS_FACTOR = 3.78541
LITERS_TO_GALLONS_FACTOR = 1 / GALLONS_TO_LITERS_FACTOR

def gallons_to_liters(gallons):
    liters = gallons * GALLONS_TO_LITERS_FACTOR
    return liters

def liters_to_gallons(liters):
    gallons = liters * LITERS_TO_GALLONS_FACTOR
    return gallons

if __name__ == '__main__':
    sample_gallons = 5.0
    sample_liters = 15.0
    
    converted_liters = gallons_to_liters(sample_gallons)
    converted_gallons = liters_to_gallons(sample_liters)
    
    print(f"{sample_gallons} gallons is {converted_liters:.2f} liters")
    print(f"{sample_liters} liters is {converted_gallons:.2f} gallons")