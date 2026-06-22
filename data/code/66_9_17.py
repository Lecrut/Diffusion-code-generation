def convert_km_to_meters(kilometers):
    return list(map(lambda km: km * 1000, kilometers))

if __name__ == '__main__':
    sample_kilometers = (1, 2.5, 3, 10)
    result = convert_km_to_meters(sample_kilometers)
    print(result)