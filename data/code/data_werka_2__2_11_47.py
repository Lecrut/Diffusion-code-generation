LITERS_TO_GALLONS_FACTOR = 0.264172

def liters_to_gallons(liters):
    return liters * LITERS_TO_GALLONS_FACTOR

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35]
    for value in sample_values:
        gallons = liters_to_gallons(value)
        print(f"{value} liters is {gallons} gallons")