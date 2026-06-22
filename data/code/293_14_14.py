def grams_to_ounces(grams: float) -> float:
    return round(grams * 0.035274, 2)

if __name__ == '__main__':
    weights = [100, 200, 300]
    ounces_weights = [grams_to_ounces(weight) for weight in weights]
    print(f"Conversion from grams to ounces: {ounces_weights}")