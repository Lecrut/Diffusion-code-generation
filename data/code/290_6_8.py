def tons_to_pounds(tons):
    return tons * 2000

if __name__ == '__main__':
    sample_tons = 1.5
    result = tons_to_pounds(sample_tons)
    print(f"{sample_tons} tons is {result:.2f} pounds")