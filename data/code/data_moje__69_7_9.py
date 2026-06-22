def miles_to_feet_generator():
    distances = (1, 5, 10, 25, 100, 500)
    for miles in distances:
        yield miles * 5280

if __name__ == '__main__':
    for feet in miles_to_feet_generator():
        print(feet)