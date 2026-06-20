CONVERSION_FACTOR = 0.621371

def kilometers_to_miles(kilometers):
    return kilometers * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_value = 5
    result = kilometers_to_miles(sample_value)
    print(result)