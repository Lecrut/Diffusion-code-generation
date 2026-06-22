def grams_to_ounces(grams: float) -> str:
    if not isinstance(grams, (int, float)) or grams < 0:
        raise ValueError("Grams must be a non-negative number.")
    
    ounces = grams * 0.035274
    return f"{ounces:.2f} oz"

if __name__ == '__main__':
    sample_grams = 100
    print(grams_to_ounces(sample_grams))