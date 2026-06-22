def km_to_meters(kilometers):
    if not isinstance(kilometers, (int, float)) or kilometers < 0:
        raise ValueError("Input must be a non-negative number")
    return kilometers * 1000

if __name__ == '__main__':
    sample_distance_km = 5
    try:
        result_meters = km_to_meters(sample_distance_km)
        print(f"Input distance in kilometers: {sample_distance_km}")
        print(f"Converted distance in meters: {result_meters}")
    except ValueError as e:
        print(e)