def convert_distance(value, unit):
    if unit == 'miles':
        return value * 1.60934
    elif unit == 'kilometers':
        return value / 1.60934
    else:
        raise ValueError("Unit must be 'miles' or 'kilometers'")

if __name__ == '__main__':
    distance_miles = 10
    distance_kilometers = convert_distance(distance_miles, 'miles')
    print(f"{distance_miles} miles is {distance_kilometers:.2f} kilometers")

    distance_miles_back = convert_distance(distance_kilometers, 'kilometers')
    print(f"{distance_kilometers:.2f} kilometers is {distance_miles_back:.2f} miles")