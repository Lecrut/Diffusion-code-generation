def compare_miles_to_kilometers(miles, kilometers):
    miles_to_km = 1.60934
    return miles * miles_to_km == kilometers

if __name__ == '__main__':
    print(compare_miles_to_kilometers(5, 8.0467))