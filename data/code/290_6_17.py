def tons_to_pounds(tons):
    try:
        pounds = tons * 2000
        return round(pounds, 2)
    except TypeError:
        raise ValueError("Input must be a number representing tons")

if __name__ == '__main__':
    sample_tons = 5.5
    result = tons_to_pounds(sample_tons)
    print(result)