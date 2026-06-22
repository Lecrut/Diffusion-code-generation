def grams_to_ounces(grams):
    if not all(isinstance(g, (int, float)) for g in grams):
        raise ValueError("All elements must be numbers.")
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    print(grams_to_ounces(sample_weights))