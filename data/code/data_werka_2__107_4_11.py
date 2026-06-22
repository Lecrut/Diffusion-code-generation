from datetime import datetime

def date_string_to_iso_format(date_input: str) -> str:
    day, month, year = date_input.split('.')
    original_date = datetime(year=int(year), month=int(month), day=int(day))
    formatted_output = original_date.strftime("%Y-%m-%d")
    return formatted_output

if __name__ == '__main__':
    sample_dates = ["12.04.2023", "30.06.1985", "15.11.2000"]
    for current_date in sample_dates:
        transformed = date_string_to_iso_format(current_date)
        print(transformed)