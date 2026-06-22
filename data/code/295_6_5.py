def grams_to_ounces(grams):
    return round(grams * 0.035274, 4)

if __name__ == '__main__':
    print(grams_to_ounces(100))
    print(grams_to_ounces(250))
    print(grams_to_ounces(500))