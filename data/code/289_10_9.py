def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return round(miles, 2)

if __name__ == '__main__':
    distance_km = 50.0
    distance_mi = kilometers_to_miles(distance_km)
    print(f"{distance_km} kilometers is equal to {distance_mi:.2f} miles.")