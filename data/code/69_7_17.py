def miles_to_feet_generator(distances):
    for distance in distances:
        yield distance * 5280

if __name__ == '__main__':
    distances = (1, 2, 3, 4, 5)
    generator = miles_to_feet_generator(distances)
    for feet in generator:
        print(feet)