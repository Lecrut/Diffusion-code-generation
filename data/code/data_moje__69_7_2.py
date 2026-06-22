def miles_to_feet_generator(distances):
    for mile in distances:
        yield mile * 5280

if __name__ == '__main__':
    sample_distances = (1, 5, 10, 20)
    generator = miles_to_feet_generator(sample_distances)
    for feet in generator:
        print(feet)