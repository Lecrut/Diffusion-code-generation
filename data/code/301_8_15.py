def convert_date_format(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    converted_lines = [line.strip().replace('/', '-', 2).replace('-', '/', 1) for line in lines]
    
    with open(file_path, 'w') as file:
        file.writelines(converted_lines)

if __name__ == '__main__':
    sample_file_path = 'dates.txt'
    convert_date_format(sample_file_path)