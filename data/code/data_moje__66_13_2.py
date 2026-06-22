FACTOR = 1000

km_to_m = lambda km: km * FACTOR

if __name__ == '__main__':
    value_in_km = 10
    result = km_to_m(value_in_km)
    print(result)