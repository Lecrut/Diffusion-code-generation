def convert_kg_to_lbs(weights_kg):
    pounds = [w * 2.20462 for w in weights_kg]
    return pounds

if __name__ == '__main__':
    sample_weights = [1, 10, 50, 100, 0.5]
    result = convert_kg_to_lbs(sample_weights)
    print(result)