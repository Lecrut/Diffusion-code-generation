conversion_factors = {'oz': 28.3495}

def ounces_to_grams(ounces):
    return int(ounces * conversion_factors['oz'])
if __name__ == '__main__':
    print(ounces_to_grams(1))
    print(ounces_to_grams(0.5))
    print(ounces_to_grams(16))