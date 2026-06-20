import datetime

def parse_and_extract_components(iso_date_str):
    date_obj = datetime.datetime.fromisoformat(iso_date_str)
    return date_obj.year, date_obj.month, date_obj.day

if __name__ == '__main__':
    sample_date = "2023-10-15T14:30:00"
    year, month, day = parse_and_extract_components(sample_date)
    print(f"Year: {year}, Month: {month}, Day: {day}")