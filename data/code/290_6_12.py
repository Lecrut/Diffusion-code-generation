def convert_tons_to_pounds(tons):
    pounds_per_ton = 2000
    return tons * pounds_per_ton

if __name__ == '__main__':
    sample_tons = 1.5
    result = convert_tons_to_pounds(sample_tons)
    print(f"{sample_tons} tons is {result:.2f} pounds")