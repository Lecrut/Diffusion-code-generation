from functools import reduce

def get_conversion_factor():
    return 1000

def multiply_km_by_factor(km_value):
    factor = get_conversion_factor()
    return km_value * factor

def convert_kilometers_to_meters(kilometers_tuple):
    return list(map(multiply_km_by_factor, kilometers_tuple))

if __name__ == '__main__':
    sample_data = (0.5, 1.0, 10.5, 100)
    result = convert_kilometers_to_meters(sample_data)
    print(result)