def convert_tons_to_pounds(tons):
    conversion_factor = {
        'ton': 2000
    }
    pounds = tons * conversion_factor['ton']
    return round(pounds, 2)

if __name__ == '__main__':
    sample_ton_value = 1.5
    result = convert_tons_to_pounds(sample_ton_value)
    print(f"{sample_ton_value} ton is {result} pounds")