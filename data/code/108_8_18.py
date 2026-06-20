import dateutil.parser

def extract_day(date_string):
    try:
        parsed_date = dateutil.parser.parse(date_string)
        return parsed_date.day
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None

if __name__ == '__main__':
    sample_date_str = '2023-10-27T14:30:00'
    day_of_month = extract_day(sample_date_str)
    if day_of_month is not None:
        print(day_of_month)