def grams_to_ounces(grams: float) -> str:
    ounces = grams * 0.035274
    return f"{ounces:.2f}"

if __name__ == '__main__':
    sample_grams = 100
    result = grams_to_ounces(sample_grams)
    print(result)