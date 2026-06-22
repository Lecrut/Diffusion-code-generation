def convert_date_format(file_path):
    with open(file_path, 'r') as file:
        dates = file.readlines()

    converted_dates = [date.strip().replace('/', '-', 2).replace('-', '/', 1) for date in dates]

    with open(file_path, 'w') as file:
        file.writelines(converted_dates)

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    convert_date_format(sample_file_path)