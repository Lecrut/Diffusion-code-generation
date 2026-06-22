def convert_km_to_m(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_km_values = [1, 2.5, 10, 0.5]
    result = convert_km_to_m(sample_km_values)
    print(result)