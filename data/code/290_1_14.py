def grams_to_ounces(grams: float) -> str:
    if not isinstance(grams, (int, float)) or grams < 0:
        raise ValueError('Input must be a non-negative number.')
    conversion_factor = 0.035274
    ounces = grams * conversion_factor
    return f'{ounces:.2f}'
if __name__ == '__main__':
    print(grams_to_ounces(16))
    print(grams_to_ounces(1000))
    print(grams_to_ounces(0.5))