def convert_km_to_m(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_values = [1.5, 2.0, 3.75, 0.001]
    result = convert_km_to_m(sample_values)
    print(result)