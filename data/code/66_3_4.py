def km_to_m(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_km = [1, 5, 10, 0.5]
    sample_m = km_to_m(sample_km)
    print(sample_m)