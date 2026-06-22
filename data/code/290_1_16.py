def grams_to_ounces(grams):
    return "{:.2f}".format(grams * 0.035274)

if __name__ == '__main__':
    print(grams_to_ounces(100))
    print(grams_to_ounces(500))