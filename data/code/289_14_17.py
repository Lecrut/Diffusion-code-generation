def nautical_miles_to_kilometers(nautical_miles):
    conversion_factor = 1.852
    kilometers = nautical_miles * conversion_factor
    return round(kilometers, 2)

if __name__ == '__main__':
    distance_in_nm = 7.25
    distance_in_km = nautical_miles_to_kilometers(distance_in_nm)
    print(f"{distance_in_nm} nautical miles is {distance_in_km} kilometers")