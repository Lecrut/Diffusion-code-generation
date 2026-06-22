def convert_miles_to_feet(miles_tuple):
    for miles in miles_tuple:
        yield miles * 5280

if __name__ == '__main__':
    distances = (1, 5, 10, 50, 100)
    for feet in convert_miles_to_feet(distances):
        print(feet)