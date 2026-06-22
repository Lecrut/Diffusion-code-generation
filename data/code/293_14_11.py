def grams_to_ounces(grams: float) -> float:
    return round(grams * 0.035274, 2)

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300]
    weights_in_ounces = [grams_to_ounces(g) for g in weights_in_grams]
    print(weights_in_ounces)