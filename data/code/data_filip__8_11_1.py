def split_and_filter(csv_string):
    parts = csv_string.split(',')
    return [part for part in parts if part]

if __name__ == '__main__':
    sample_data = "apple,banana,,cherry,,date,"
    result = split_and_filter(sample_data)
    print(result)