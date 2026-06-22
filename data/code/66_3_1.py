def km_to_meters(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2.0, 0.5, 10.25]
    meters_result = km_to_meters(sample_kilometers)
    print(meters_result)