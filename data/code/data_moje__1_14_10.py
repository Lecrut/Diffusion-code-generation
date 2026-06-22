def convert_kg_to_pounds(kg_values):
    return [kg * 2.20462 for kg in kg_values]
if __name__ == '__main__':
    sample_kg = [50, 60, 75, 85, 100]
    pounds = convert_kg_to_pounds(sample_kg)
    print(pounds)