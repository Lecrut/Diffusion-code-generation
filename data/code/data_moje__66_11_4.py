def convert_km_to_m(kilometer_values):
    result = []
    for value in kilometer_values:
        meters = value * 1000
        result.append(meters)
    return result

if __name__ == '__main__':
    sample_values = [1.5, 2, 0.5, 10, 0.001]
    print(convert_km_to_m(sample_values))