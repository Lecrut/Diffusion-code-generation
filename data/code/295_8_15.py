CUBIC_METER_TO_CUBIC_FOOT = 35.3147

def cubic_meters_to_cubic_feet(cubic_meters):
    return int(cubic_meters * CUBIC_METER_TO_CUBIC_FOOT)

if __name__ == '__main__':
    sample_cubic_meters = 10
    sample_cubic_feet = cubic_meters_to_cubic_feet(sample_cubic_meters)
    print(f"{sample_cubic_meters} cubic meters is equal to {sample_cubic_feet} cubic feet")