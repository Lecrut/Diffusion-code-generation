def miles_to_feet_generator(distances):
    FEET_PER_MILE = 5280
    for mile in distances:
        yield mile * FEET_PER_MILE

if __name__ == '__main__':
    sample_distances = (1, 5, 10, 26)
    for value in miles_to_feet_generator(sample_distances):
        print(value)