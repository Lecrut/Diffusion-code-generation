def convert_km_to_m(kilometers_tuple):
    conversion_factor = 1000
    return tuple(map(lambda x: x * conversion_factor, kilometers_tuple))

if __name__ == '__main__':
    sample_km = (1.5, 2, 3.75, 10)
    result_m = convert_km_to_m(sample_km)
    print(result_m)