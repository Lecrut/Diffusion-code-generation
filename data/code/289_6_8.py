CONVERSION_FACTOR = 1 / 1000

def grams_to_kilograms(grams):
    return grams * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_grams = 2500
    print(f"{sample_grams} grams is {grams_to_kilograms(sample_grams)} kilograms")
    
    large_sample_grams = 1500000
    print(f"{large_sample_grams} grams is {grams_to_kilograms(large_sample_grams)} kilograms")