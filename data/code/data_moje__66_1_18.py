METERS_PER_KILOMETER = 1000

def convert_km_to_meters(kilometers):
    return kilometers * METERS_PER_KILOMETER

if __name__ == '__main__':
    sample_kilometers = 5
    result = convert_km_to_meters(sample_kilometers)
    print(result)