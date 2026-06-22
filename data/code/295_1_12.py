conversion_factor = {
    'L': 0.264172,
    'G': 3.78541
}

def liters_to_gallons(liters):
    return liters * conversion_factor['L']

if __name__ == '__main__':
    sample_liters = 10
    gallons = liters_to_gallons(sample_liters)
    print(f"{sample_liters} L is {gallons:.2f} G")