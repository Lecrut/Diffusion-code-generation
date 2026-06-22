def miles_to_feet_generator(miles_tuple):
    for miles in miles_tuple:
        yield miles * 5280

if __name__ == '__main__':
    distances = (1, 2, 5, 10)
    for feet in miles_to_feet_generator(distances):
        print(feet)