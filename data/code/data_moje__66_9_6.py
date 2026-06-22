def convert_km_to_m(km_tuple):
    return tuple(map(lambda km: km * 1000, km_tuple))

if __name__ == '__main__':
    km_data = (1, 2.5, 10, 0.75)
    print(convert_km_to_m(km_data))