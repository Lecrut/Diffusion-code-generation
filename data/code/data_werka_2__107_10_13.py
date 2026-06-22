from datetime import datetime

SOURCE_FORMAT = "%Y-%m-%d"
TARGET_FORMAT = "%d/%m/%Y"

def convert_date_format(date_string: str) -> str:
    date_object = datetime.strptime(date_string, SOURCE_FORMAT)
    return date_object.strftime(TARGET_FORMAT)

if __name__ == '__main__':
    hard_coded_date = "2024-01-15"
    converted_date = convert_date_format(hard_coded_date)
    print(converted_date)