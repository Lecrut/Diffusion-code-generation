def process_csv_string(csv_data):
    parts = csv_data.split(',')
    result = []
    for part in parts:
        if part != '':
            result.append(part)
    return result

if __name__ == '__main__':
    sample_input = 'apple,banana,,cherry,,date,,'
    filtered_result = process_csv_string(sample_input)
    print(filtered_result)