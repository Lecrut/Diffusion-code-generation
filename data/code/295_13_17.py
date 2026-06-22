GALLONS_TO_LITERS_FACTOR = 3.78541
LITERS_TO_GALLONS_FACTOR = 1 / GALLONS_TO_LITERS_FACTOR

def gallons_to_liters(gallons):
    return gallons * GALLONS_TO_LITERS_FACTOR

def liters_to_gallons(liters):
    return liters * LITERS_TO_GALLONS_FACTOR

if __name__ == '__main__':
    sample_gallons = 3.5
    sample_liters = 14.0
    
    print(f"{sample_gallons} gallons is {gallons_to_liters(sample_gallons)} liters")
    print(f"{sample_liters} liters is {liters_to_gallons(sample_liters)} gallons")