def liters_to_gallons(liters):
    if not isinstance(liters, (int, float)):
        raise ValueError("Volume must be a number")
    conversion_rate = 0.264172
    return liters * conversion_rate

if __name__ == '__main__':
    sample_values = [0.5, 12.3, 25.6, 50.0]
    for value in sample_values:
        print(f"{value} liters is {liters_to_gallons(value)} gallons")