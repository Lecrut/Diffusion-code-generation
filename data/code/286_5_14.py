def nanometers_to_meters(nanometers):
    return nanometers * 1e-09
if __name__ == '__main__':
    sample_value = 1500000000
    result = nanometers_to_meters(sample_value)
    print(result)