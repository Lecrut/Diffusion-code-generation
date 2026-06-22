CONVERSION_RATE = {'kilometers_to_miles': 5}

def convert_distance(distance, conversion_type):
    if conversion_type not in CONVERSION_RATE:
        raise ValueError("Unsupported conversion type")
    return distance * CONVERSION_RATE[conversion_type]

if __name__ == '__main__':
    sample_kilometers = 15
    miles = convert_distance(sample_kilometers, 'kilometers_to_miles')
    print(miles)