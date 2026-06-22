def miles_to_centimeters(miles):
    conversion_factor = 160934
    if miles < 0:
        raise ValueError("Distance cannot be negative.")
    return miles * conversion_factor

if __name__ == '__main__':
    distance_in_miles = 5
    try:
        distance_in_cm = miles_to_centimeters(distance_in_miles)
        print(f"{distance_in_miles} miles is equal to {distance_in_cm} centimeters.")
    except ValueError as e:
        print(e)