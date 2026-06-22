def grams_to_kilograms(grams):
    return grams / 1000

if __name__ == '__main__':
    sample_grams = 2500
    print(f"{sample_grams} grams is {grams_to_kilograms(sample_grams)} kilograms")
    
    large_sample_grams = 1500000
    print(f"{large_sample_grams} grams is {grams_to_kilograms(large_sample_grams)} kilograms")