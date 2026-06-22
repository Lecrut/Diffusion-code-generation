def convert_kg_to_pounds(weights):
    conversion_factor = 2.20462
    return [w * conversion_factor for w in weights]

if __name__ == '__main__':
    sample_weights = [1, 5, 10, 20, 50, 100]
    pounds = convert_kg_to_pounds(sample_weights)
    print(pounds)