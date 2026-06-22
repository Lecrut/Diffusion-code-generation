def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles * 1.60934

def main():
    distance_in_km = 10.0
    miles = convert_kilometers_to_miles(distance_in_km)
    print(f"{distance_in_km} kilometers is equal to {miles} miles")

    distance_in_mi = 5.0
    km = convert_miles_to_kilometers(distance_in_mi)
    print(f"{distance_in_mi} miles is equal to {km} kilometers")

if __name__ == '__main__':
    main()