def convert_weight_ratios(ratios):
    return [float(x) / float(y) for x, y in ratios]
if __name__ == '__main__':
    sample_ratios = [(1000000000, 250000000), (987654321, 123456789), (1000000000000, 500000000)]
    converted_ratios = convert_weight_ratios(sample_ratios)
    print(converted_ratios)