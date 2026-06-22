def km_to_meters(kilometers):
    meters = kilometers * 1000
    return meters

if __name__ == '__main__':
    sample_distance_km = 50
    result_meters = km_to_meters(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {result_meters}")