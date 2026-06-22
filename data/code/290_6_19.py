def tons_to_pounds(tons):
    return tons * 2000

if __name__ == '__main__':
    sample_tons = 3.5
    result = tons_to_pounds(sample_tons)
    print(f"{result:.2f} pounds")