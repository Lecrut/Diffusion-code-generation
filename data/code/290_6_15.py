def tons_to_pounds(tons):
    return tons * 2000

if __name__ == '__main__':
    sample_tons = 5.5
    pounds = tons_to_pounds(sample_tons)
    print(f"{pounds:.2f}")