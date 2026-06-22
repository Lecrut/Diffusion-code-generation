conversion_factor = 35.3147

def cubic_meters_to_cubic_feet(cubic_meters):
    return int(cubic_meters * conversion_factor)

if __name__ == '__main__':
    sample_volume_cubic_meters = 250
    sample_volume_cubic_feet = cubic_meters_to_cubic_feet(sample_volume_cubic_meters)
    print(f"{sample_volume_cubic_meters} cubic meters is equal to {sample_volume_cubic_feet} cubic feet")