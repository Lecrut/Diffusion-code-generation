def convert_distance(distance, unit):
    if unit == 'km':
        return distance * 0.621371
    elif unit == 'mi':
        return distance / 0.621371
    else:
        raise ValueError("Invalid unit. Use 'km' for kilometers or 'mi' for miles.")

if __name__ == '__main__':
    distance_km = 10
    distance_mi = 5

    converted_to_miles = convert_distance(distance_km, 'km')
    converted_to_kilometers = convert_distance(distance_mi, 'mi')

    print(f"{distance_km} kilometers is {converted_to_miles:.2f} miles")
    print(f"{distance_mi} miles is {converted_to_kilometers:.2f} kilometers")