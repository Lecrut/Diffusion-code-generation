def grams_to_milligrams(grams):
    return grams * 1000

if __name__ == '__main__':
    weight_grams = 250
    weight_milligrams = grams_to_milligrams(weight_grams)
    print(f"{weight_grams} grams is {weight_milligrams} milligrams")