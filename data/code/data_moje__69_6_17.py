MILES_TO_FEET = 5280

def convert_miles_to_feet(miles):
    return miles * MILES_TO_FEET

if __name__ == '__main__':
    distance_miles = 10
    distance_feet = convert_miles_to_feet(distance_miles)
    print(distance_feet)