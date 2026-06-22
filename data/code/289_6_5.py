def grams_to_kilograms(grams):
    return grams / 1000

if __name__ == '__main__':
    sample_grams = 5000
    print(f"{sample_grams} grams is {grams_to_kilograms(sample_grams)} kilograms")