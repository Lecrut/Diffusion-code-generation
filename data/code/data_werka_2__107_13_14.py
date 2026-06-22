from datetime import datetime

def transform_date_format(raw_date: str) -> str:
    parsed_dt = datetime.strptime(raw_date, "%Y/%m/%d")
    month_name = parsed_dt.strftime("%B")
    day_part = parsed_dt.strftime("%d")
    year_part = parsed_dt.strftime("%Y")
    return f"{month_name} {int(day_part)}, {year_part}"

if __name__ == '__main__':
    original_string = "1999/12/31"
    formatted_output = transform_date_format(original_string)
    print(formatted_output)