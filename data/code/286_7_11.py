def picometers_to_meters(picometers):
    return picometers * 1e-12

if __name__ == '__main__':
    sample_value = 500_000_000
    result = picometers_to_meters(sample_value)
    print(result)