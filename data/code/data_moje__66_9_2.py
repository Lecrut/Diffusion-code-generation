def multiply_by_one_thousand(value):
    return value * 1000

def convert_km_tuple_to_meters(km_tuple):
    return tuple(map(multiply_by_one_thousand, km_tuple))

if __name__ == '__main__':
    sample_kilometers = (0.5, 1.25, 4.75, 10, 100.5)
    result = convert_km_tuple_to_meters(sample_kilometers)
    print(result)