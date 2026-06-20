def process_csv_string(csv_data):
    return [item for item in csv_data.split(',') if item]

if __name__ == '__main__':
    sample_data = "apple,banana,,cherry,,,date"
    result = process_csv_string(sample_data)
    print(result)