def liters_to_gallons(liters):
    conversion_rate = 0.264172
    gallons = liters * conversion_rate
    return gallons

if __name__ == '__main__':
    sample_values = [0.5, 1.0, 3.0, 6.0]
    for value in sample_values:
        converted_value = liters_to_gallons(value)
        print(f"{value} liters is {converted_value} gallons")