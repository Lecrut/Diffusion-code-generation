def grams_to_ounces(grams: float) -> float:
    return round(grams * 0.035274, 2)

if __name__ == '__main__':
    weight_in_grams = 1000.0
    weight_in_ounces = grams_to_ounces(weight_in_grams)
    print(f"Conversion from {weight_in_grams} grams to ounces: {weight_in_ounces} oz")