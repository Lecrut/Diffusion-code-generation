conversion_factor = 1.852

def nautical_miles_to_kilometers(nautical_miles):
    if nautical_miles == 0:
        return 0
    return nautical_miles * conversion_factor

if __name__ == '__main__':
    distances_km = {
        0: nautical_miles_to_kilometers(0),
        1: nautical_miles_to_kilometers(1),
        10: nautical_miles_to_kilometers(10),
        100: nautical_miles_to_kilometers(100)
    }
    
    for nautical_miles, distance_km in distances_km.items():
        print(f"{nautical_miles} nautical miles is {distance_km} kilometers")