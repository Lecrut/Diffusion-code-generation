from dateutil import parser

def extract_day_of_week(date_str):
    try:
        date_obj = parser.parse(date_str)
        return date_obj.strftime('%A')
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    day_of_week = extract_day_of_week(sample_date)
    print(day_of_week)