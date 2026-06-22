def kilometers_to_meters(kilometers):
    return kilometers * 1000

if __name__ == '__main__':
    sample_distance_km = 42.5
    result_meters = kilometers_to_meters(sample_distance_km)
    print(result_meters)