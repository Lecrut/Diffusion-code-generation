def convert_millimeters_to_inches(millimeters):
    conversion_factors = {'mm': 1 / 25.4}
    return millimeters * conversion_factors['mm']
if __name__ == '__main__':
    sample_value = 2540
    result = convert_millimeters_to_inches(sample_value)
    print(result)