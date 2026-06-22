import calendar
import datetime

MONTH_ABBREVIATIONS: dict[str, int] = {
    name: index
    for index, name in enumerate(calendar.month_abbr)
    if index > 0
}

def convert_date_format(date_string: str) -> str:
    parts = date_string.split("-")
    day_part: str = parts[0]
    month_part: str = parts[1]
    year_part: str = parts[2]

    month_number: int = MONTH_ABBREVIATIONS[month_part]
    
    date_object: datetime.date = datetime.date(
        int(year_part),
        month_number,
        int(day_part)
    )
    
    return date_object.strftime("%Y%m%d")

if __name__ == "__main__":
    sample_input: str = "15-Mar-2022"
    output_string: str = convert_date_format(sample_input)
    print(output_string)