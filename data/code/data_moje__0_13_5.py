def convert_kilometers_to_miles(kilometers):
    miles = kilometers / 5
    return miles

if __name__ == '__main__':
    distance_km = 10
    result = convert_kilometers_to_miles(distance_km)
    print(result)