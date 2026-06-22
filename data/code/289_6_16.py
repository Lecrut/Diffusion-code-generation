def grams_to_kilograms(grams):
    kilogram = grams / 1000
    return kilogram

if __name__ == '__main__':
    sample_grams = 7500
    print(f"{sample_grams} grams is {grams_to_kilograms(sample_grams)} kilograms")
    large_sample_grams = 3000000
    print(f"{large_sample_grams} grams is {grams_to_kilograms(large_sample_grams)} kilograms")