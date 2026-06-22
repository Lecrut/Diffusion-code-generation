def cubic_meters_to_cubic_feet(cubic_meters):
    return int(round(cubic_meters * 35.3147, 0))

if __name__ == '__main__':
    sample_value = 10
    result = cubic_meters_to_cubic_feet(sample_value)
    print(result)