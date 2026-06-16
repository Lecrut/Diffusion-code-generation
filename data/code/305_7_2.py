import datetime
def process_dates(input_filename, output_filename):
    date_objects = []
    try:
        with open(input_filename, 'r') as infile:
            for line in infile:
                try:
                    date_str = line.strip()
                    if date_str:
                        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                        date_objects.append(date_obj)
                except ValueError:
                    continue
    except FileNotFoundError:
        return
    date_objects.sort()
    with open(output_filename, 'w') as outfile:
        for date_obj in date_objects:
            outfile.write(date_obj.strftime('%Y-%m-%d') + '\n')
if __name__ == '__main__':
    input_file = "input_dates.txt"
    output_file = "sorted_dates.txt"
    with open(input_file, 'w') as f:
        f.write("2023-10-26\n")
        f.write("2023-10-25\n")
        f.write("2023-10-27\n")
        f.write("2023-10-24\n")
        f.write("2023-10-26\n")
    process_dates(input_file, output_file)