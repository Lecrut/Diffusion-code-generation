def grams_to_kilograms(grams):
    if not isinstance(grams, (int, float)):
        raise ValueError("Input must be an integer or float")
    return grams / 1000

if __name__ == '__main__':
    print(f"2500 grams is {grams_to_kilograms(2500)} kilograms")
    print(f"1500000 grams is {grams_to_kilograms(1500000)} kilograms")