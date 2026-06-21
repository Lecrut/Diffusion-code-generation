from datetime import datetime

INPUT_FORMAT = "%Y-%m-%d"
OUTPUT_FORMAT = "%d/%m/%Y"

def convert_date_format(date_input: str) -> str:
    date_object = datetime.strptime(date_input, INPUT_FORMAT)
    formatted_output = date_object.strftime(OUTPUT_FORMAT)
    return formatted_output

if __name__ == '__main__':
    raw_date = "2024-12-31"
    converted_date = convert_date_format(raw_date)
    print(converted_date)