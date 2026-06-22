CONVERSION_FACTOR = 1000.0

def convert_kilometers_to_meters(kilometers):
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    kilometer_value = 5
    result = convert_kilometers_to_meters(kilometer_value)
    print(result)