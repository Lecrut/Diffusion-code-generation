def grams_to_kilograms(grams):
    return grams / 1000

if __name__ == '__main__':
    small_sample_grams = 2500
    print(f"{small_sample_grams} grams is {grams_to_kilograms(small_sample_grams)} kilograms")
    
    large_sample_grams = 1500000
    result = grams_to_kilograms(large_sample_grams)
    print(f"{large_sample_grams} grams is {result} kilograms")