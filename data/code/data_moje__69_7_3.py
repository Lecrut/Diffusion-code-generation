def miles_to_feet_generator(distances):
    for miles in distances:
        yield miles * 5280

if __name__ == '__main__':
    sample_distances = (1, 2, 3, 10, 50, 100)
    for feet_value in miles_to_feet_generator(sample_distances):
        print(feet_value)