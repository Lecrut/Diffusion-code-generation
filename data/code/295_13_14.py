GALLONS_TO_LITERS_FACTOR = 3.78541
LITERS_TO_GALLONS_FACTOR = 0.264172

def gallons_to_liters(gallons):
    return gallons * GALLONS_TO_LITERS_FACTOR

def liters_to_gallons(liters):
    return liters * LITERS_TO_GALLONS_FACTOR

if __name__ == '__main__':
    sample_gallons = 3.5
    sample_liters = 14.299585
    
    print(f"{sample_gallons} gallons is equal to {gallons_to_liters(sample_gallons):.2f} liters")
    print(f"{sample_liters} liters is equal to {liters_to_gallons(sample_liters):.2f} gallons")