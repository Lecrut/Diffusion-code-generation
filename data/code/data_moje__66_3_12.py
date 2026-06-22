def km_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_km = [1.5, 3.0, 0.25, 7.89]
    print(km_to_meters(sample_km))