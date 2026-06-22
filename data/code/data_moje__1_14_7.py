def convert_kg_to_pounds(kilograms):
    return kilograms * 2.20462

if __name__ == '__main__':
    sample_weights = [1, 5, 10, 25, 50, 100]
    for weight in sample_weights:
        result = convert_kg_to_pounds(weight)
        print(f"{weight} kg = {result} lbs")