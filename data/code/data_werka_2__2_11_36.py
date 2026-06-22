def convert_liters_to_gallons(liters):
    if not isinstance(liters, (int, float)):
        raise ValueError("Volume must be a number")
    return liters * 0.264172

if __name__ == '__main__':
    sample_values = [0.5, 2.0, 5.0, 10.0]
    for value in sample_values:
        print(f"{value} liters is {convert_liters_to_gallons(value)} gallons")