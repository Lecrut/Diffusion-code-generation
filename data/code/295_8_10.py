CUBIC_METER_TO_CUBIC_FOOT_FACTOR = 35.3147

def cubic_meters_to_cubic_feet(cubic_meters):
    return int(cubic_meters * CUBIC_METER_TO_CUBIC_FOOT_FACTOR)

if __name__ == '__main__':
    sample_cubic_meters = 10
    result_cubic_feet = cubic_meters_to_cubic_feet(sample_cubic_meters)
    print(result_cubic_feet)