def milligrams_to_grams(milligrams):
    return round(milligrams / 1000.0, 3)
if __name__ == '__main__':
    print(milligrams_to_grams(500))
    print(milligrams_to_grams(2500))