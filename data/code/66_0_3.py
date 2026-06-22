METERS_PER_KILOMETER = 1000

def convert_kilometers_to_meters(distance_km):
    return distance_km * METERS_PER_KILOMETER

if __name__ == '__main__':
    test_value = 12.5
    output = convert_kilometers_to_meters(test_value)
    print(output)