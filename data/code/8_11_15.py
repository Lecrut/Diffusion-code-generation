def process_csv(csv_string: str) -> list:
    parts = csv_string.split(',')
    return [p for p in parts if p != '']

if __name__ == '__main__':
    sample_data = "apple,banana,,cherry,,date"
    result = process_csv(sample_data)
    print(result)