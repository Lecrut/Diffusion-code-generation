def kilometers_to_meters(kilometers: float) -> float:
    return kilometers * 1000.0

if __name__ == '__main__':
    sample_distance_km = 15.75
    result_meters = kilometers_to_meters(sample_distance_km)
    print(result_meters)