CONVERSION_FACTOR = 1000.0

def convert_kilometers_to_meters(kilometers: float) -> float:
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_kilometers = 50
    result_meters = convert_kilometers_to_meters(sample_kilometers)
    print(result_meters)