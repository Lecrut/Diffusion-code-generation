def miles_to_feet_generator(miles_tuple):
    for miles in miles_tuple:
        yield miles * 5280

if __name__ == '__main__':
    distances = (1, 2, 3.5, 10)
    feet_values = list(miles_to_feet_generator(distances))
    print(feet_values)