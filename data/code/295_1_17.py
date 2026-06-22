LITERS_TO_GALLONS = 0.264172

def liters_to_gallons(liters):
    return liters * LITERS_TO_GALLONS

if __name__ == '__main__':
    sample_liters = 10.0
    conversion_factor = liters_to_gallons(sample_liters)
    print(f"{sample_liters} liters is equal to {conversion_factor:.4f} gallons")