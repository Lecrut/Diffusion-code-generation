def kilometers_to_meters(kilometers):
    meters = kilometers * 1000
    return meters

if __name__ == '__main__':
    sample_distance_km = 50
    distance_in_meters = kilometers_to_meters(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {distance_in_meters}")