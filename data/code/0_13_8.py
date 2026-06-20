def convert_kilometers_to_miles(kilometers):
    return kilometers / 5.0

if __name__ == '__main__':
    distance_km = 100
    distance_mi = convert_kilometers_to_miles(distance_km)
    print(distance_mi)