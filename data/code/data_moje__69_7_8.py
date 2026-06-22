def convert_miles_to_feet(mile_distances):
    for miles in mile_distances:
        yield miles * 5280

if __name__ == '__main__':
    sample_distances = (1, 5, 10, 100, 1000)
    result = convert_miles_to_feet(sample_distances)
    for feet_value in result:
        print(feet_value)