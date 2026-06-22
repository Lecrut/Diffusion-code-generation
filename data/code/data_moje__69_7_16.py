def feet_per_mile_generator(distances):
    for miles in distances:
        yield miles * 5280

if __name__ == '__main__':
    distances = (1, 2.5, 10, 0.5, 100)
    generator = feet_per_mile_generator(distances)
    feet_values = list(generator)
    print(feet_values)