def miles_to_feet_generator(distances_miles):
    for mile in distances_miles:
        yield mile * 5280

if __name__ == '__main__':
    sample_distances = (1, 2, 5, 10, 25, 50, 100)
    converter = miles_to_feet_generator(sample_distances)
    for feet_value in converter:
        print(feet_value)