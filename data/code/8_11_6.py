def filter_csv_string(csv_string):
    parts = csv_string.split(',')
    return [part for part in parts if part != '']

if __name__ == '__main__':
    sample_csv = "apple,,banana,,cherry,,date,,elderberry"
    result = filter_csv_string(sample_csv)
    print(result)