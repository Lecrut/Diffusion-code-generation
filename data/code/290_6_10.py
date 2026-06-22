def convert_tons_to_pounds(tons):
    if tons < 0:
        raise ValueError('Mass cannot be negative.')
    conversion_factor = 2204.62
    pounds = tons * conversion_factor
    return round(pounds, 2)
if __name__ == '__main__':
    sample_tons = 1.5
    result = convert_tons_to_pounds(sample_tons)
    print(result)