DISTANCES_MILES = (1, 2, 5, 10, 50, 100, 1000, 5000, 10000, 52800)

def miles_to_feet_generator(mile_distances):
    for miles in mile_distances:
        yield miles * 5280

if __name__ == '__main__':
    for feet in miles_to_feet_generator(DISTANCES_MILES):
        print(feet)