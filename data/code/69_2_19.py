MILES_TO_FEET_FACTOR = 5280
distance_conversion = lambda miles: miles * MILES_TO_FEET_FACTOR

if __name__ == '__main__':
    print(distance_conversion(1))
    print(distance_conversion(5))
    print(distance_conversion(12.5))