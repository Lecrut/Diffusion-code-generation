CONVERSION_FACTOR = 1 / 1000

def grams_to_kilograms(grams):
    return grams * CONVERSION_FACTOR

if __name__ == '__main__':
    print(f"2500 grams is {grams_to_kilograms(2500)} kilograms")
    print(f"1500000 grams is {grams_to_kilograms(1500000)} kilograms")