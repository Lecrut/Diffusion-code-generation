def convert_liters_to_gallons(liters):
    conversion_rate = 0.264172
    gallons = liters * conversion_rate
    return gallons

if __name__ == '__main__':
    sample_values = [5.0, 10.0, 15.0, 25.0]
    for value in sample_values:
        converted_value = convert_liters_to_gallons(value)
        print(f"{value} liters is {converted_value} gallons")