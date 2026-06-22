def tons_to_pounds(tons):
    conversion_factor = 2000
    return tons * conversion_factor

if __name__ == '__main__':
    sample_tons = 3.5
    pounds = tons_to_pounds(sample_tons)
    print(f"{sample_tons} tons is {pounds:.2f} pounds")