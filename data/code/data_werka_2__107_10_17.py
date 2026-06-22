from datetime import datetime

INPUT_FORMAT = "%Y-%m-%d"
OUTPUT_FORMAT = "%d/%m/%Y"
SAMPLE_DATE = "2023-01-15"

def convert_date_format(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, INPUT_FORMAT)
    return date_obj.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    formatted_date = convert_date_format(SAMPLE_DATE)
    print(formatted_date)