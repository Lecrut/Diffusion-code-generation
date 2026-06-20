def process_csv_string(csv_data: str) -> list:
    parts = csv_data.split(',')
    return [part for part in parts if part != '']

if __name__ == '__main__':
    data = "apple,banana,,cherry,,date"
    result = process_csv_string(data)
    print(result)