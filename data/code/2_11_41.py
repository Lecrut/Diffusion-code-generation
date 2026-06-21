def liters_to_gallons(liters):
    conversion_rate = 0.264172
    return liters * conversion_rate

if __name__ == '__main__':
    sample_values = [4, 8, 12, 16]
    for value in sample_values:
        print(f"{value} liters is {liters_to_gallons(value)} gallons")