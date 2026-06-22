def kilometers_to_meters(km_list):
    return [km * 1000 for km in km_list]

if __name__ == '__main__':
    sample_km = [1.5, 2.0, 0.75, 10.0]
    result = kilometers_to_meters(sample_km)
    print(result)