def convert_date_format(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    converted_lines = []
    for line in lines:
        date_parts = line.strip().split('/')
        if len(date_parts) == 3:
            month, day, year = date_parts
            converted_line = f'{day}/{month}/{year}\n'
            converted_lines.append(converted_line)

    with open(file_path, 'w') as file:
        file.writelines(converted_lines)

if __name__ == '__main__':
    sample_file_path = 'sample_dates.txt'
    convert_date_format(sample_file_path)