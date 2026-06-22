KILometers_TO_METERS_FACTOR = 1000

def convert_kilometers_to_meters(kilometers):
    return kilometers * KILometers_TO_METERS_FACTOR

if __name__ == '__main__':
    sample_kilometers = 5
    result = convert_kilometers_to_meters(sample_kilometers)
    print(result)