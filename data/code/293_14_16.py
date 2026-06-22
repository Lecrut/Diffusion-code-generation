def grams_to_ounces(grams: list) -> list:
    return [round(g * 0.035274, 2) for g in grams]

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300]
    weights_in_ounces = grams_to_ounces(weights_in_grams)
    print(f"Weights in ounces: {weights_in_ounces}")