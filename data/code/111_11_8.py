from datetime import datetime

def parse_iso_date(iso_string):
    date_obj = datetime.fromisoformat(iso_string)
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    return year, month, day

if __name__ == '__main__':
    sample_date = '2023-10-05T14:30:00'
    year, month, day = parse_iso_date(sample_date)
    print(f'Year: {year}, Month: {month}, Day: {day}')