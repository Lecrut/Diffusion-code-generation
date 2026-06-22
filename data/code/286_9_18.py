def nautical_miles_to_kilometers(nautical_miles):
    conversion_factor = 1.852
    return nautical_miles * conversion_factor

if __name__ == '__main__':
    distance_km = nautical_miles_to_kilometers(0)
    print(f"0 nautical miles is {distance_km} kilometers")
    distance_km = nautical_miles_to_kilometers(2.5)
    print(f"2.5 nautical miles is {distance_km} kilometers")
    distance_km = nautical_miles_to_kilometers(100)
    print(f"100 nautical miles is {distance_km} kilometers")