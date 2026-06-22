def convert_km_to_m(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    sample_kilometers = [1, 2.5, 10, 0.5]
    meters = convert_km_to_m(sample_kilometers)
    print(meters)