def pounds_to_ounces(pounds):
    ounces = int(pounds * 16)
    return ounces
if __name__ == '__main__':
    sample_pounds = 3.5
    result = pounds_to_ounces(sample_pounds)
    print(result)