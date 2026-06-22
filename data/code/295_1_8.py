conversion_factors = {
    'L_to_G': 0.264172,
}

def liters_to_gallons(liters):
    return liters * conversion_factors['L_to_G']

if __name__ == '__main__':
    sample_liters = 10
    gallons = liters_to_gallons(sample_liters)
    print(f"{sample_liters} L is {gallons:.2f} G")