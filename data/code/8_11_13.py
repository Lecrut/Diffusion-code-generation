def process_csv_data(data_string):
    parts = data_string.split(',')
    filtered_parts = []
    for part in parts:
        if part.strip() != '':
            filtered_parts.append(part.strip())
    return filtered_parts

if __name__ == '__main__':
    sample_input = "apple, ,banana,,cherry, , date, "
    result = process_csv_data(sample_input)
    print(result)