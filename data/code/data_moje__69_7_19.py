DISTANCES = (1, 2, 5, 10)

def miles_to_feet(miles):
    return miles * 5280

def generate_feet(distances):
    for mile in distances:
        yield miles_to_feet(mile)

if __name__ == '__main__':
    for feet in generate_feet(DISTANCES):
        print(feet)