import re

def convert_date_format(date_str):
    match = re.match(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_str)
    if match:
        return f"{match.group(2)}/{match.group(1)}/{match.group(3)}"
    return None

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    formatted_lines = [convert_date_format(line.strip()) for line in lines if convert_date_format(line.strip())]

    with open(file_path, 'w') as file:
        file.writelines([f"{line}\n" for line in formatted_lines])

if __name__ == '__main__':
    sample_file_path = 'sample_dates.txt'
    process_file(sample_file_path)
    print(f"Dates in {sample_file_path} have been converted and saved back to the same file.")