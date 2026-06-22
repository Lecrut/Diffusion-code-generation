def grams_to_kilograms(grams):
    return grams / 1000

if __name__ == '__main__':
    sample_grams = 3750
    result = grams_to_kilograms(sample_grams)
    print(f"{sample_grams} grams is {result} kilograms")
    
    large_sample_grams = 2500000
    large_result = grams_to_kilograms(large_sample_grams)
    print(f"{large_sample_grams} grams is {large_result} kilograms")