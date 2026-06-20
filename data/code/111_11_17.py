import datetime

def parse_iso_date(date_str):
    return datetime.datetime.fromisoformat(date_str).date()

if __name__ == '__main__':
    date1 = '2023-10-15T14:30:00'
    parsed_date = parse_iso_date(date1)
    year = parsed_date.year
    month = parsed_date.month
    day = parsed_date.day
    print(f"Year: {year}, Month: {month}, Day: {day}")