def process_csv_string(csv_string):
    return [item for item in csv_string.split(',') if item]
if __name__ == '__main__':
    sample_csv = 'apple,,banana,orange,,grape,pear'
    result = process_csv_string(sample_csv)
    print(result)