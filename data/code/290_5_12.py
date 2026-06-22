CONVERSION_FACTOR_OZ_TO_GR = 28.3495

def convert_ounces_to_grams(ounces):
    grams = ounces * CONVERSION_FACTOR_OZ_TO_GR
    return int(round(grams))
if __name__ == '__main__':
    print(convert_ounces_to_grams(1))
    print(convert_ounces_to_grams(3.5))