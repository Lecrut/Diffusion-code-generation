def convert_kg_to_pounds(kilograms):
    return kilograms * 2.20462

if __name__ == '__main__':
    sample_weights = [10, 20, 30, 45.5, 100]
    for weight in sample_weights:
        print(convert_kg_to_pounds(weight))