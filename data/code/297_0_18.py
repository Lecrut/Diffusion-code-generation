def meters_to_kilometers(meters):
    kilometers = meters / 1000
    return kilometers

if __name__ == '__main__':
    sample_meters = 5000.0
    result_km = meters_to_kilometers(sample_meters)
    print(result_km)