def filter_non_empty_csv_values(csv_string):
    parts = csv_string.split(',')
    return [part for part in parts if part != '']

if __name__ == '__main__':
    sample_data = "apple,banana,,cherry,,date,,elderberry"
    result = filter_non_empty_csv_values(sample_data)
    print(result)