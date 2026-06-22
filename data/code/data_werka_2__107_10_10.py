from datetime import datetime

SOURCE_FORMAT = "%Y-%m-%d"
TARGET_FORMAT = "%d/%m/%Y"

def convert_date_format(date_string: str) -> str:
    date_object = datetime.strptime(date_string, SOURCE_FORMAT)
    formatted_date = date_object.strftime(TARGET_FORMAT)
    return formatted_date

if __name__ == '__main__':
    raw_date = "1999-12-31"
    output_date = convert_date_format(raw_date)
    print(output_date)