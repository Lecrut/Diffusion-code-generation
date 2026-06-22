def feet_generator(miles):
    for mile in miles:
        yield mile * 5280

if __name__ == '__main__':
    distances = (1, 2, 3, 4, 5)
    generator = feet_generator(distances)
    feet_values = list(generator)
    print(feet_values)