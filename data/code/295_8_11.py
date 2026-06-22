def cubic_meters_to_cubic_feet(cubic_meters):
    conversion_factor = 35.3147
    cubic_feet = cubic_meters * conversion_factor
    return int(round(cubic_feet))

if __name__ == '__main__':
    sample_cubic_meters = 50
    result_cubic_feet = cubic_meters_to_cubic_feet(sample_cubic_meters)
    print(f"{sample_cubic_meters} cubic meters is equal to {result_cubic_feet} cubic feet")