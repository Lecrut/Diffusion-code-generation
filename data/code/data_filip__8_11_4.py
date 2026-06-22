def process_csv_string(csv_data: str) -> list:
    raw_parts = csv_data.split(',')
    result = [part for part in raw_parts if part != '']
    return result

if __name__ == '__main__':
    sample_data = "apple,,banana,,cherry,"
    filtered_values = process_csv_string(sample_data)
    print(filtered_values)