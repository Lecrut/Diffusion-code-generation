from datetime import datetime

MONTH_NAMES = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def format_date_string(date_input: str) -> str:
    parts = date_input.split("-")
    day = int(parts[0])
    month = MONTH_NAMES[parts[1]]
    year = int(parts[2])
    date_obj = datetime(year, month, day)
    return date_obj.strftime("%Y%m%d")

if __name__ == '__main__':
    input_date = "15-Mar-2022"
    output_date = format_date_string(input_date)
    print(output_date)