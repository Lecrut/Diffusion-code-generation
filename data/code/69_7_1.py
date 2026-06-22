def convert_miles_to_feet(miles_tuple):
    for mile in miles_tuple:
        yield mile * 5280

if __name__ == '__main__':
    sample_distances = (1, 5, 10, 25, 100)
    generator = convert_miles_to_feet(sample_distances)
    for value in generator:
        print(value)