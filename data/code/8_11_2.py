def process_csv_string(data: str) -> list:
    parts = data.split(',')
    result = []
    for part in parts:
        if part != '':
            result.append(part)
    return result

if __name__ == '__main__':
    sample_data = "apple,banana,,orange,,grape,,"
    filtered_items = process_csv_string(sample_data)
    print(filtered_items)