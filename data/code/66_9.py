def convert_km_to_meters(kilometers):
    return list(map(lambda km: km * 1000, kilometers))

if __name__ == '__main__':
    km_tuple = (1, 2.5, 3, 5.75, 10)
    print(convert_km_to_meters(km_tuple))