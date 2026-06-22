def convert_miles_to_feet(distances):
    for mile in distances:
        yield mile * 5280

if __name__ == '__main__':
    sample_distances = (1, 2, 3, 5, 10, 25, 50, 100, 500, 1000)
    generator = convert_miles_to_feet(sample_distances)
    for value in generator:
        print(value)