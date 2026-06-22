import datetime

SOURCE_FORMAT = "%d.%m.%Y"
TARGET_FORMAT = "%Y-%m-%d"

def format_date(date_string: str) -> str:
    parsed_date = datetime.datetime.strptime(date_string, SOURCE_FORMAT)
    formatted_date = parsed_date.strftime(TARGET_FORMAT)
    return formatted_date

if __name__ == '__main__':
    test_inputs = ["12.05.1990", "30.11.2021", "01.01.2000"]
    for current_input in test_inputs:
        output = format_date(current_input)
        print(output)