def ounces_to_grams(ounces):
    try:
        grams = ounces * 28.3495
        return grams
    except TypeError:
        return "Invalid input"

if __name__ == '__main__':
    print(ounces_to_grams(10))
    print(ounces_to_grams('a'))