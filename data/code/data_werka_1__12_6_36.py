def convert_weight_ratios(ratios):
    return [int(x * 1000) / 1000.0 for x in ratios]
if __name__ == '__main__':
    sample_values = [123456789, 987654321, 456789123, 321654987]
    converted_ratios = convert_weight_ratios(sample_values)
    print(converted_ratios)