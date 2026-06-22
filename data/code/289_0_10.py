conversion_table = {
    'kilometers_to_meters': 1000,
}

def km_to_meters(kilometers):
    return kilometers * conversion_table['kilometers_to_meters']

if __name__ == '__main__':
    sample_distance_km = 5
    result_meters = km_to_meters(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {result_meters}")