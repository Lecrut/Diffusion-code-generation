LITERS_TO_GALLONS_CONVERSION_FACTOR = 0.264172

def convert_liters_to_gallons(liters):
    if not isinstance(liters, (int, float)):
        raise ValueError("Volume must be a number")
    return liters * LITERS_TO_GALLONS_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_values = [0.5, 2.0, 4.0, 8.0]
    for value in sample_values:
        print(f"{value} liters is {convert_liters_to_gallons(value)} gallons")