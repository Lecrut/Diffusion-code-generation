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
        print(f"Error: Input file {input_filename} not found.")
        return
    date_objects.sort()
    try:
        with open(output_filename, 'w') as outfile:
            for date_obj in date_objects:
                outfile.write(date_obj.strftime('%Y-%m-%d') + '\n')
    except IOError:
        print(f"Error: Could not write to output file {output_filename}.")
if __name__ == '__main__':
    input_file = "input_dates.txt"
    output_file = "sorted_dates.txt"
    sample_data = [
        "2023-10-26",
        "2023-10-25",
        "2023-10-27",
        "2023-10-24"
    ]
    with open(input_file, 'w') as f:
        for date in sample_data:
            f.write(date + '\n')
    process_dates(input_file, output_file)