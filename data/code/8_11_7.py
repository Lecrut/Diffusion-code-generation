def process_csv_string(csv_data):
    parts = csv_data.split(',')
    return [part for part in parts if part]

if __name__ == '__main__':
    sample_data = "apple,,banana, ,cherry,,"
    result = process_csv_string(sample_data)
    print(result)