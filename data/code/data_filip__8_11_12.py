def process_csv_string(csv_string):
    parts = csv_string.split(',')
    return [part for part in parts if part != '']

if __name__ == '__main__':
    sample = "apple,,banana,orange,,,kiwi"
    result = process_csv_string(sample)
    print(result)