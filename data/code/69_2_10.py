FEET_PER_MILE = 5280
miles_to_feet = lambda miles: miles * FEET_PER_MILE
if __name__ == '__main__':
    distance_miles = 7
    result = miles_to_feet(distance_miles)
    print(result)