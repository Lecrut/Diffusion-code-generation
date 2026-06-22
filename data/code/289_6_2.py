def grams_to_kilograms(grams):
    kilogram = grams / 1000
    return kilogram

if __name__ == '__main__':
    sample_grams = 2500
    sample_kilograms = grams_to_kilograms(sample_grams)
    print(f"{sample_grams} grams is {sample_kilograms} kilograms")
    
    large_sample_grams = 1500000
    large_sample_kilograms = grams_to_kilograms(large_sample_grams)
    print(f"{large_sample_grams} grams is {large_sample_kilograms} kilograms")