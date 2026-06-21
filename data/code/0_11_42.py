DISTANCE_CONVERSIONS = {'kilometers_to_miles': 5}

def convert_distance(kilometers):
    conversion_factor = DISTANCE_CONVERSIONS.get('kilometers_to_miles')
    if conversion_factor is None:
        raise ValueError("Unsupported conversion type")
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = 20
    miles = convert_distance(sample_kilometers)
    print(miles)