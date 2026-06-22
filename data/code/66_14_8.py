KILOMETERS_TO_METERS_FACTOR = 1000

def convert_distance_kilometers_to_meters(distance_in_kilometers):
    return distance_in_kilometers * KILOMETERS_TO_METERS_FACTOR

if __name__ == '__main__':
    test_value = 42.5
    output = convert_distance_kilometers_to_meters(test_value)
    print(output)