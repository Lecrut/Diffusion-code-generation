def ounces_to_grams(ounces):
    return int(round(ounces * 28.3495, 0))

if __name__ == '__main__':
    print(ounces_to_grams(1))
    print(ounces_to_grams(0.5))
    print(ounces_to_grams(10))