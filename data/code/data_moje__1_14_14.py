def kg_to_pounds(kg):
    return kg * 2.20462
if __name__ == '__main__':
    sample_weights_kg = [0, 50, 70, 100, 150]
    results = [kg_to_pounds(kg) for kg in sample_weights_kg]
    print(results)