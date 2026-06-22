def validate_km(kilometers):
    if not isinstance(kilometers, (int, float)) or kilometers < 0:
        raise ValueError("Input must be a non-negative number representing kilometers.")
    
def km_to_meters(kilometers):
    validate_km(kilometers)
    meters = kilometers * 1000
    return meters

if __name__ == '__main__':
    sample_distance_km = 5.5
    result_meters = km_to_meters(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {result_meters}")