def gallons_to_liters(gallons):
    conversion_factor = 3.78541
    liters = gallons * conversion_factor
    return liters

def liters_to_gallons(liters):
    conversion_factor = 0.264172
    gallons = liters * conversion_factor
    return gallons

if __name__ == '__main__':
    sample_gallons = 3.5
    sample_liters = 14.35995
    
    print(f"{sample_gallons} gallons is equal to {gallons_to_liters(sample_gallons):.2f} liters")
    print(f"{sample_liters} liters is equal to {liters_to_gallons(sample_liters):.2f} gallons")