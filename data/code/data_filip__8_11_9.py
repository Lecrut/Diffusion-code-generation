def process_csv_string(data):
    if not data:
        return []
    parts = data.split(',')
    result = []
    for part in parts:
        if part != '':
            result.append(part)
    return result

if __name__ == '__main__':
    sample_data = "apple,,banana,,cherry,,"
    filtered_items = process_csv_string(sample_data)
    print(filtered_items)