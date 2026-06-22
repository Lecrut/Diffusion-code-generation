def ounces_to_grams(ounces):
    conversion_factor = 28.3495
    grams = ounces * conversion_factor
    return int(round(grams))
if __name__ == '__main__':
    sample_ounces = 10.5
    result = ounces_to_grams(sample_ounces)
    print(result)