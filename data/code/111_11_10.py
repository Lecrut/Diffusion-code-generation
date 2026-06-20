from datetime import datetime

def parse_iso_date(iso_string):
    date_obj = datetime.fromisoformat(iso_string)
    return date_obj.year, date_obj.month, date_obj.day

if __name__ == '__main__':
    sample_date = "2023-10-05T14:30:00Z"
    year, month, day = parse_iso_date(sample_date)
    print(f"Year: {year}, Month: {month}, Day: {day}")