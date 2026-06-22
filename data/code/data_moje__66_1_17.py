CONVERSION_FACTOR = 1000.0

def km_to_meters(kilometers):
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kilometers = 5
    result = km_to_meters(sample_kilometers)
    print(result)