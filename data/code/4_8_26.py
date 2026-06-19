def convert_distance(distance, unit):
    if unit == 'km':
        return distance * 0.621371
    elif unit == 'miles':
        return distance / 0.621371
    else:
        raise ValueError("Invalid unit. Use 'km' or 'miles'.")

if __name__ == '__main__':
    distance_km = 10
    converted_miles = convert_distance(distance_km, 'km')
    print(f"{distance_km} km is {converted_miles:.2f} miles")

    distance_miles = 5
    converted_km = convert_distance(distance_miles, 'miles')
    print(f"{distance_miles} miles is {converted_km:.2f} km")