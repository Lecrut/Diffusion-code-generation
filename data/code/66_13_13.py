KMS_PER_METER = 0.001

km_to_m = lambda km: km / KMS_PER_METER

if __name__ == '__main__':
    sample_km = 5
    meters = km_to_m(sample_km)
    print(meters)